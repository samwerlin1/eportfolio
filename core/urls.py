from django.urls import path

from . import views

urlpatterns = [
    path("", views.hellotime, name="hellotime"),
    path("screenprint", views.screenprint, name="screenprint"),
]