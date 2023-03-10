from django.urls import path
from . import views

urlpatterns = [
    path("articles/", views.articles, name="articles"),
    path("", views.home, name="home")
]