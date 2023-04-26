from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # process form data and save to database
            return render(request, 'home.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'website/sign_up.html', {'form': form})
