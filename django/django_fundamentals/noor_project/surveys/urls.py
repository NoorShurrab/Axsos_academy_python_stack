# URL routing for the surveys app.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),   # List all surveys     
    path('new/', views.new), # Form to add a new survey  
]

