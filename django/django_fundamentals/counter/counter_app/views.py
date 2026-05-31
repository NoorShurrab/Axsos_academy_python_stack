from django.shortcuts import render, redirect

# Initializes session counter to 0 on first visit, increments it on subsequent visits.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return render(request, 'index.html')

# Deletes the session counter if it exists, then redirects to the index page.
def destroy_session(request):
    if 'counter' in request.session:
        del request.session['counter']
    return redirect('/')

# Increments the session counter by 1 if it exists, then redirects to the index page.
def increment_two(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    return redirect('/')