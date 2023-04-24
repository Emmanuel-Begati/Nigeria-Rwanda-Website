from django.shortcuts import render




# Create your views here.
def home(request):
    return render(request, 'website/index.html')
def contact(request):
    return render(request, 'website/contact_us.html')
def about(request):
    return render(request, 'website/about.html')
def login(request):
    return render(request, 'website/login.html')
def sign_up(request):
    return render(request, 'website/sign_up.html')