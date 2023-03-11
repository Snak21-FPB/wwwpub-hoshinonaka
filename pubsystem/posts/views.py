from django.views import generic

class TopView(generic.TemplateView):
    template_name = "posts/top.html"
    