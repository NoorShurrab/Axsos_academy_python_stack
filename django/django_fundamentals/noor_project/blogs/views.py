# View functions for all blog routes: handles redirects, text responses, and JSON output
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# 1. http://127.0.0.1:8000/
# def root(request):
#     return redirect('/blogs')

# 2. http://127.0.0.1:8000/blogs
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# 3. http://127.0.0.1:8000/blogs/new
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# 4. http://127.0.0.1:8000/blogs/create
def create(request):
    return redirect('/blogs/')

# 5. http://127.0.0.1:8000/blogs/<number>
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# 6. http://127.0.0.1:8000/blogs/<number>/edit
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# 7. http://127.0.0.1:8000/blogs/<number>/delete
def destroy(request, number):
    return redirect('/blogs')

# 8. http://127.0.0.1:8000/blogs/json 
# def json_bonus(request):
#     data = {
#         "title": "My first blog",
#         "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."
#     }
#     return JsonResponse(data)