from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


def login_view(request):
    next_url = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
        return redirect('animal_list')
    context = {'form': form, }
    return render(request, 'users/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('animal_list')


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('animal_list')
    context = {'form': form, }
    return render(request, 'users/signup.html', context)
