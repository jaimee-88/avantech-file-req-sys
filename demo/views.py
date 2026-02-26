from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def home(request):
    """Home page with contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form is valid - you can add custom logic here
            form = ContactForm()  # Reset form after submission
    else:
        form = ContactForm()
    
    return render(request, 'home.html', {'form': form})
