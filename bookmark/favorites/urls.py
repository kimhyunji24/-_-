# favorites/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_list, name='favorite_list'),
    path('add/', views.add_favorite, name='add_favorite'),
]