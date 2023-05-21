from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def home(request):
    return render(request, 'website/index.html')
def resources(request):
    return render(request, 'website/resources.html')
def contact(request):
    return render(request, 'website/contact_us.html')
def about(request):
    return render(request, 'website/about.html')
def login(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('website-home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
     else: 
         return render(request, 'users/login.html')
        


def logout_view(request):
    logout(request)
    return redirect('website-home')