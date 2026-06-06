#  Handles all user-related route responses.
#  Currently returns placeholder text for each route.
from django.shortcuts import render, HttpResponse

# Handles both /register route
def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

# Handles the /login route
def login(request):
    return HttpResponse("placeholder for users to log in.")

# Reuses the register view for the /users/new route
def new(request):
    return register(request) 

# Handles the /users route — lists all users
def index(request):
    return HttpResponse("placeholder to display all the list of users later.")
