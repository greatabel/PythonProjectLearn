from django.urls import path

from . import views

urlpatterns = [
    path('index_v1', views.index, name='index_v1    '),
    path('index', views.index, name='index'),
]