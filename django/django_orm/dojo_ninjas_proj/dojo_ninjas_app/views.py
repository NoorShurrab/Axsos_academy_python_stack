# Views for Dojos & Ninjas app
# Handles rendering the index page and processing
# creation/deletion of Dojos and Ninjas.
from django.shortcuts import render, redirect
from .models import Dojo, Ninja


# Fetches all Dojo objects and passes them to the template.
def index(request):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)

# Accepts POST data (name, city, state) and creates a new Dojo.
# Redirects back to index after creation.
def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state']
        )
    return redirect("/")

# Accepts POST data (first_name, last_name, dojo_id).
# Fetches the selected Dojo by ID and links the new Ninja to it.
# Redirects back to index after creation.
def create_ninja(request):
    if request.method == "POST":
        selected_dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        
        Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo=selected_dojo
        )
    return redirect("/")


# Fetches a Dojo by its ID and deletes it.
# All related Ninjas are automatically deleted via CASCADE.
# Redirects back to index after deletion.
def delete_dojo(request, dojo_id):
    dojo_to_delete = Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()
    return redirect("/")