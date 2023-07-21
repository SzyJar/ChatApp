from django.shortcuts import render, redirect
from django.contrib.auth import login
# Create your views here.

from .forms import SignUpForm

def indexPage(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})
