from django.views.generic import FormView

from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginView(FormView):
    template_name = 'users/signup.html'
    model = CustomUser
    form_class = AuthenticationForm


class RegistrationView(FormView):
    template_name = 'users/signup.html'
    model = CustomUser
    form_class = UserCreationForm
