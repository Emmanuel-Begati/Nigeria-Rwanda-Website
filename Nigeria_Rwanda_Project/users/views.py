from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)


        if form.is_valid():
            # process form data and save to database
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {username}')
            return redirect('website-home')
    else:
        form = SignUpForm()
    return render(request, 'website/sign_up.html', {'form': form})
    
    
