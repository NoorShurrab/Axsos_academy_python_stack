# Views for Books & Authors app (many-to-many)
from django.shortcuts import render, redirect
from .models import Book, Author

# Fetches all books and renders the Book.html template,
# which includes the "Add a Book" form and a table of all books.
def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'Book.html', context)

# Accepts POST data (title, desc) and creates a new Book.
# Redirects back to the books index.
def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
    return redirect('/')

# Fetches a single book by ID and passes it to View_book.html, along with all authors NOT yet associated with this book
def show_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    context = {
        'book': current_book,
        'available_authors': Author.objects.exclude(books=current_book)
    }
    return render(request, 'View_book.html', context)

# Adds the selected author (from dropdown) to the given book's
# many-to-many "authors" relationship.
# Redirects back to the book's detail page.
def join_author(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{book_id}')

# Fetches all authors and renders the Author.html template,
# which includes the "Add an Author" form and a table of all authors.
def authors_index(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'Author.html', context)

# Accepts POST data (first_name, last_name, notes) and creates a new Author 
# Redirects back to the authors index.
def add_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
    return redirect('/authors')

# Fetches a single author by ID and passes it to View_author.html,
# along with all books NOT yet associated with this author
def show_author(request, author_id):
    current_author = Author.objects.get(id=author_id)
    context = {
        'author': current_author,
        'available_books': Book.objects.exclude(authors=current_author)
    }
    return render(request, 'View_author.html', context)

# Adds the selected book (from dropdown) to the given author's
# many-to-many "books" relationship.
# Redirects back to the author's detail page.
def join_book(request, author_id):
    if request.method == "POST":
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{author_id}')