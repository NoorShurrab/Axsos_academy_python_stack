# Views for the Users app — handles displaying, creating, and deleting users from the database.
from django.shortcuts import render, redirect
from .models import User

# Fetches all users from the database and renders the main page.
def index(request):
    context = {
        "all_users": User.objects.all() # Retrieve every User record
    }
    return render(request, "index.html", context)

# Reads form data from the request, creates a new User record,
# then redirects back to the index page.
def create_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email_address']
        age = request.POST['age']
        
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_address=email,
            age=age
        )
    return redirect("/")

# Looks up the User by primary key, deletes the record,
# then redirects back to the index page.
def delete_user(request, user_id):
    user_to_delete = User.objects.get(id=user_id) # Fetch user by ID
    user_to_delete.delete() # Remove from DB
    
    return redirect("/")