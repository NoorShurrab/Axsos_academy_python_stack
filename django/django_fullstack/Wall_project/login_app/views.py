# Handles user registration, login, session management,
# and logout using bcrypt for password hashing
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Renders the home page with login and registration forms
def index(request):
    return render(request, 'index.html')

# Register - POST - validates registration data. If there are errors, sends them as flash messages and redirects to '/'.
# Otherwise, hashes the password, creates the new user, starts a session, and redirects to '/success'.
def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            
            new_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                birthday = request.POST['birthday'],
                password = password_hash
            )

            messages.success(request, "Registration successful! Please log in to your account.", extra_tags='success-msg')
            return redirect('/login')
    return redirect('/')

# login - POST - validates login credentials. If there are errors, sends them as flash messages and redirects to '/'.
# Otherwise, starts a session for the user and redirects to '/success'.
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/login') 
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            return redirect('/wall/')
            
    return render(request, 'login.html')

# success - displays the success page only for logged-in users.
# Redirects to '/' if no active session is found.
def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'success.html')

# logout - clears the session and redirects to '/'
def logout(request):
    request.session.flush() 
    return redirect('/login')