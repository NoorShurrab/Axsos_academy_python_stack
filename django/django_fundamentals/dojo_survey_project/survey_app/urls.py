# Maps the root URL to the survey form and /result to the submitted data page
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),          
    path('result', views.result),   
]