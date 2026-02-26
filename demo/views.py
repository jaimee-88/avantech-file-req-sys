from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def home(request):
    """Home page view"""
    return render(request, 'home.html')

def contact(request):
    """Contact form view with email sending"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            try:
                # Send email
                send_mail(
                    subject=f"Contact Form: {subject}",
                    message=f"From: {name} ({email})\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Email sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
