from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import Newsletter

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            newsletter = Newsletter(email=email)
            newsletter.save()
        return render(request, 'contact_form/contact_success.html', {'form': form})
            
    else:
        form = NewsletterForm()
    return render(request, 'subscribe.html', {'form': form})