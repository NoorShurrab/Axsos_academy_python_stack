# Maps three routes to their respective views for handling session-related operations.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                                    
    path('destroy_session', views.destroy_session),         
    path('increment_two', views.increment_two),
]