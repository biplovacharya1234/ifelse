from django.urls import path
# from current folder(. means current folder) import views
from . import views
urlpatterns = [
    path('', views.index),
    path('trending', views.trending)
]
