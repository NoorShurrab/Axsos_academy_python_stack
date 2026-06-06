# blogs/urls.py
# Maps URL patterns to their corresponding view functions for the blogs app
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.root),                          
    path('', views.index),      # Displays a list of all blogs              
    path('new/', views.new),    # Displays a form to create a new blog
    path('create/', views.create),    # Creates a new blog            
    path('<int:number>/', views.show),   # Displays details of a specific blog 
    path('<int:number>/edit/', views.edit),   # Displays a form to edit an existing blog  
    path('<int:number>/delete/', views.destroy), # Deletes a specific blog 
    #path('blogs/json', views.json_bonus),            
]