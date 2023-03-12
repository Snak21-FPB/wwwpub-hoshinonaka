from django.contrib.auth import views


class AccountLoginView(views.LoginView):
    template_name = "accounts/login.html"

class AccountLogoutView(views.LogoutView):
    pass