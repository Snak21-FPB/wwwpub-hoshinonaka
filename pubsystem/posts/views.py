from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class TopView(generic.TemplateView):
    template_name = "posts/top.html"


class HomeView(LoginRequiredMixin ,generic.TemplateView):
    template_name = "posts/home.html"
