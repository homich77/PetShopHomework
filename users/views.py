from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, UserLoginForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('animal_list')  # Redirect to a success page.
    context = {'form': form, }
    return render(request, 'users/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('animal_list')


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')  # UserCreationForm has fields with names pass1 and pass2
        user.set_password(password)
        user.save()
        if user is not None:
            login(request, user)
            return redirect('animal_list')
        else:
            print("Still None")
    context = {'form': form, }
    return render(request, 'users/signup.html', context)
