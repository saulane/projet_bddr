from django.urls import path,re_path
from . import views

urlpatterns = [
    path("articles/", views.articles, name="articles"),
    path("articles/<path:doi>/", views.article),
    path("", views.home, name="home")
]