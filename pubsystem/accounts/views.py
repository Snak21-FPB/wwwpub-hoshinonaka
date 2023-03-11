from django.contrib.auth import views
from django.views import generic


class AccountLoginView(views.LoginView):
    template_name = "accounts/login.html"
