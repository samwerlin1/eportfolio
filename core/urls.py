from django.urls import path

from . import views

urlpatterns = [
    # Home page loads page built in the about.html html template file
    path('', views.about_view, name='about_page'),

    # Each of these pages show clickable cards for all projects tagged with that skill
    path('skill/<slug:skill_slug>/', views.skill_page_view, name='skill_page'),

    # Individual project pages (could have been either built as own html file or with components through admin interface)
    path('<slug:slug>/', views.page_detail_view, name='page_detail'),
]