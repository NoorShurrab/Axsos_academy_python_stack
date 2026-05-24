# First Django Project
A Django web application that practices project setup, app creation, URL routing, and returning responses from views.

## Setup Instructions
1. Create a new Django project
    - django-admin startproject noor_project
    - cd noor_project

2. Create a new app
    - python manage.py startapp blogs

3. Register the app
    - In **noor_project/settings.py**, add **'blogs'** to **INSTALLED_APPS**.

4. Configure URLs
    - In noor_project/urls.py — include routes for root / and /blogs
    - In blogs/urls.py — define all blog-specific routes

5. Run the server
    - python manage.py runserver

## Routes
| URL | Function | Action |
|-----|----------|--------|
| `/` | root | Redirects to `/blogs` |
| `/blogs` | index | Placeholder for list of all blogs |
| `/blogs/new` | new | Placeholder for new blog form |
| `/blogs/create` | create | Redirects to `/` |
| `/blogs/<number>` | show | Displays blog by number |
| `/blogs/<number>/edit` | edit | Placeholder for edit form |
| `/blogs/<number>/delete` | destroy | Redirects to `/blogs` |

8. /blogs/json 
    - returns a JsonResponse with the following structure
        - {
            "title": "My first blog",
            "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit."
          }