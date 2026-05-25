# Renders the current date and time to the template using datetime formatting
from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now() # get the current date and time
    # %b: name of the month (e.g., Oct)
    # %d: day of the month (e.g., 26)
    # %Y: full year (e.g., 2013)
    # %I:%M %p: hour and minute in 12-hour format with AM/PM
    context = {
        "date": now.strftime("%b %d, %Y"),
        "time": now.strftime("%I:%M %p")
    }
    
    return render(request, 'index.html', context)