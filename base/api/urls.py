from django.urls import path
from django.http import JsonResponse
from . import views

urlpatterns = [
    path('api/user', views.Get, name='api'),
]