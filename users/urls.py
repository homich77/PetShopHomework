from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login_view'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration_view'),
]
