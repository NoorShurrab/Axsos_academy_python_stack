from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),        # URL pattern for the index view, which will display the list of users and the form to add a new user         
    path('create_user', views.create_user), # URL pattern for creating a user, which will handle POST requests from the form
    path('delete_user/<int:user_id>', views.delete_user), # URL pattern for deleting a user, with user_id as a parameter
]