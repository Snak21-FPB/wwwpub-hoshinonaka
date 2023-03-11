from django.contrib.auth import views


class AccountLoginView(views.LoginView):
    template_name = "accounts/login.html"
