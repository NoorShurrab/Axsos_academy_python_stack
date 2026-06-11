from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Renders index page with all dojos & ninjas
    path('create_dojo', views.create_dojo),  # Creates a new Dojo
    path('create_ninja', views.create_ninja), #  Creates a new Ninja linked to a Dojo
    path('delete_dojo/<int:dojo_id>', views.delete_dojo), # Deletes a Dojo and all its associated Ninjas
]