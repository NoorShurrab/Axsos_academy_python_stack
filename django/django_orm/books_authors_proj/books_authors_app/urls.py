# URL configuration for the Books & Authors app.
# Maps URL patterns to their corresponding views.
from django.urls import path
from . import views

urlpatterns = [
    # Books urls
    path('', views.index, name='books_index'),
    path('books/add', views.add_book, name='add_book'),
    path('books/<int:book_id>', views.show_book, name='show_book'),
    path('books/<int:book_id>/add_author', views.join_author, name='join_author'),
    
    # Authors urls
    path('authors', views.authors_index, name='authors_index'),
    path('authors/add', views.add_author, name='add_author'),
    path('authors/<int:author_id>', views.show_author, name='show_author'),
    path('authors/<int:author_id>/add_book', views.join_book, name='join_book'),
]
