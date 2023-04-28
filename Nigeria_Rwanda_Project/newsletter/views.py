from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import Newsletter
from django.http import JsonResponse



def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
                email = form.cleaned_data['email']
                newsletter = Newsletter(email=email)
                newsletter.save()
        return render(request, 'newsletter/newsletter_success.html', {'form': form})

    else:
        form = NewsletterForm()
    return render(request, 'subscribe.html', {'form': form})

def check_email(request):
    email = request.GET.get('email')
    if Newsletter.objects.filter(email=email).exists():
        data = {
            'exists': True,
            'message': 'Email already subscribed.'
        }
    else:
        data = {'exists': False}
    return JsonResponse(data)