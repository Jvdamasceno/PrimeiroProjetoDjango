from django import urls
from django.urls import path
from .views import IndexView, PratosView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pratos/<int:pk>', PratosView.as_view(), name='pratos'),
]
