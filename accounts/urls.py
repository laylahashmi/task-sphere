from django.urls import path
from accounts.views import user_login


urlPatterns = [path("login/", user_login, name="login")]
