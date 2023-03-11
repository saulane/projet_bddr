from django.urls import path,re_path
from . import views

urlpatterns = [
    path("articles/", views.articles, name="articles"),
    path("articles/<path:doi>/", views.article),
    path("", views.home, name="home"),
    path(r'api/play_count_by_month', views.articles_count_by_month, name='play_count_by_month'),
    path(r'api/play_count_by_year', views.articles_count_by_year, name='play_count_by_year'),
    path(r'api/play_count_by_week', views.articles_count_by_week, name='play_count_by_week')
]