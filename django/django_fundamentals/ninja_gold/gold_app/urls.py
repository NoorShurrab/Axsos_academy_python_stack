from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Renders the main page and initializes session variables
    path('process_money', views.process_money, name='process_money'), # Calculates gold earned/lost based on chosen location
    path('reset', views.reset, name='reset'), # Flushes the session and restarts the game
]