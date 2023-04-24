from django.shortcuts import render




# Create your views here.
def home(request):
    return render(request, 'website/index.html')
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
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
    return render(request, 'website/login.html')
def sign_up(request):
    return render(request, 'website/sign_up.html')
