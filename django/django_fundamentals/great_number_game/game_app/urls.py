from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),     # Root URL mapped to index view                  
    path('guess', views.guess),    # URL for handling guess submissions mapped to guess view             
    path('play_again', views.play_again),     # URL for resetting the game mapped to play_again view
]