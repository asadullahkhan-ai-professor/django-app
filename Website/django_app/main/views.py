from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    return render(request, 'contact.html', {'form': form})

