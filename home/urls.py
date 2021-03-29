from django.urls import path
from .views import home
from .views import index

urlpatterns = [
     path('', home),
     path('/base', index),
]
