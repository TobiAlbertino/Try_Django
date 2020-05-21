from django.shortcuts import render
#import forms
from .forms import ContactForm
# Create your views here.

def index(request):

    contact_form = ContactForm()
    context = {
        'heading' : 'Contact form',
        'content' : 'konten',
        'data_form' : contact_form,
    }
    return render(request, 'contact/index.html', context)