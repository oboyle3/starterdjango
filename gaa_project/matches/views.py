from django.shortcuts import render
from django.shortcuts import render
from .models import Match
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
def home(request):
    matches = Match.objects.all()
    return render(request, 'matches/home.html', {'matches': matches})



@login_required
def logged_in_screen(request):
    return render(request, 'matches/logged_in_screen.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'matches/signup.html', {'form': form})