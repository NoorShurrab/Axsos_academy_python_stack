# views.py - Semi-Restful TV Shows
# Handles CRUD operations for the Show model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Show


# Redirects to the shows table
def root(request):
    return redirect('/shows')

# Displays all shows in a table
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_show.html', context)

# Renders the form to add a new show
def new(request):
    return render(request, 'add_show.html')

# CREATE - POST - adds the new show to the database then redirects to the new show's detail page
def create(request):
    if request.method == "POST":
        new_show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']
        )
        return redirect(f'/shows/{new_show.id}')
    return redirect('/shows/new')

# Displays a single show's details
def show_detail(request, id):
    context = {
        'show': get_object_or_404(Show, id=id)
    }
    return render(request, 'detail_show.html', context)

# UPDATE - GET - renders the form pre-filled with show data
def edit(request, id):
    context = {
        'show': get_object_or_404(Show, id=id) # Get the show with the given id, or return 404 if not found
    }
    return render(request, 'edit_show.html', context)

# UPDATE - POST - updates the show in the database
# then redirects to the show's detail page
def update(request, id):
    if request.method == "POST":
        show = get_object_or_404(Show, id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show.id}')
    return redirect(f'/shows/{id}/edit')

# DELETE - removes the show from the database
# then redirects to the shows list
def destroy(request, id):
    show = get_object_or_404(Show, id=id)
    show.delete()
    return redirect('/shows')
