from django.urls import path

from . import views

urlpatterns = [
    path("", views.aboutme, name="aboutme"),
    path("screenprint", views.screenprint, name="screenprint"),
    path("blackbox", views.blackbox, name="blackbox"),

]