# URL routing for the users app.
# Includes user-related routes (register, login, users/new, users)
# and reuses the blogs index view for the root route 
# the root route uses the same method as /blogs.
from django.urls import path
from . import views
from blogs import views as blogs_views

urlpatterns = [
    path('', blogs_views.index),  # NINJA BONUS: root route reuses the blogs index view 
    path('register/', views.register),   # User registration page
    path('login/', views.login),     # User login page    
    path('users/new/', views.new),   # /users/new shares the same view as /register    
    path('users/', views.index),     # List all users    
]