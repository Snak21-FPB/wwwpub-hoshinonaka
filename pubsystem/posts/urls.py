from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("bureau/<slug:keyword>/", views.BureauDetailView.as_view(), name="bureau"),
]
