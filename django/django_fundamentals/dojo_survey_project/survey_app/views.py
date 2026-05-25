# Renders the survey form on GET, and displays submitted POST data on the result page
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    context = {
        'name': request.POST.get('name'), # Retrieves the value of the 'name' field from the POST data
        'location': request.POST.get('location'), # Retrieves the value of the 'location' field from the POST data
        'language': request.POST.get('language'), # Retrieves the value of the 'language' field from the POST data
        'comment': request.POST.get('comment'), # Retrieves the value of the 'comment' field from the POST data
    }
    return render(request, 'result.html', context) # Renders the 'result.html' template with the context containing the submitted form data
