from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Bureau


class TopView(generic.TemplateView):
    template_name = "posts/top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bureaus"] = Bureau.objects.all()
        return context


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "posts/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bureaus"] = Bureau.objects.all()
        return context

class BureauDetailView(generic.DetailView):
    model = Bureau
    template_name = "posts/bureau.html"
    slug_field = "keyword"
    slug_url_kwarg = "keyword"
    context_object_name = "bureau"
