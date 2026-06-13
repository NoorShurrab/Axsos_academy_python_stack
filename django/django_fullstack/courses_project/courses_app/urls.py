from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                                      
    path('courses/create', views.create),                   
    path('courses/destroy/<int:id>', views.destroy_confirm),    
    path('courses/delete/<int:id>', views.delete),       
]       