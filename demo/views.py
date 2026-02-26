from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def home(request):
    """Home page view"""
    return render(request, 'home.html')

def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form is valid - you can add custom logic here
            # For now, just display the form again
            form = ContactForm()
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
