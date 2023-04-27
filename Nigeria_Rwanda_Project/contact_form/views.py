from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
import csv

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # save the data to the database
            contact = Contact.objects.create(name=name, email=email, message=message)
            contact.save()
            
    else:
        form = ContactForm()
    return render(request, 'contact_form/contact_us.html', {'form': form})

