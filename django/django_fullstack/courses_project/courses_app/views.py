# Handles create, read, and delete operations for the Course
# model, including a one-to-one Description relationship
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Description

# Displays the form and a table of all courses
def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

# CREATE - POST - validates the submitted data. 
# If there are errors, sends them as flash messages and redirects to '/'.
# Otherwise, creates the new Course and its related Description, then redirects to '/'.
def create(request):
    if request.method == "POST":
        errors = Course.objects.create_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            new_course = Course.objects.create(name=request.POST['name'])
            Description.objects.create(course=new_course, content=request.POST['description'])
            
        return redirect('/')
    return redirect('/')

# Displays a confirmation page before deleting the course with the specified id
def destroy_confirm(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course': course
    }
    return render(request, 'destroy.html', context)

# DELETE - POST - deletes the course with the specified id (if confirmed), then redirects to '/'
def delete(request, id):
    if request.method == "POST":
        course = get_object_or_404(Course, id=id)
        course.delete() 
    return redirect('/')
