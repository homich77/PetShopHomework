from django import forms
from django.contrib.auth import authenticate

from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
        return super(LoginForm, self).clean(*args, **kwargs)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password',
        )
