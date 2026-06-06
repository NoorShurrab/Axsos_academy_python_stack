# Handles all survey-related route responses.
# Currently returns placeholder text for each route.
from django.shortcuts import render, HttpResponse

# Handles the /surveys route — lists all surveys
def index(request):
    return HttpResponse("placeholder to display all the surveys created.")

# Handles the /surveys/new route — form to add a new survey
def new(request):
    return HttpResponse("placeholder for users to add a new survey.")
