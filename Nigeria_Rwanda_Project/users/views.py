from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)


        if form.is_valid():
            # process form data and save to database
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('website-login')
    else:
        form = SignUpForm()
    return render(request, 'website/sign_up.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'users/profile.html')