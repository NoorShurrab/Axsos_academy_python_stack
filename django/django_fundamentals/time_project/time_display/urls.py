## Maps the root URL to the index view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
]