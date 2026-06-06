# Multiple Apps
A Django project that combines three independent apps (blogs, surveys, users) under one project.

## How it Run

1. Create a new Django project
```bash
   django-admin startproject noor_project
   cd noor_project
```

2. Create the three apps
```bash
   python manage.py startapp blogs
   python manage.py startapp surveys
   python manage.py startapp users
```

3. Register the apps in `settings.py`
```python
   INSTALLED_APPS = [
       ...
       'blogs',
       'surveys',
       'users',
   ]
```

5. Run the development server
```bash
   python manage.py runserver
```

6. Open your browser and go to `http://localhost:8000/`


## Apps & Routes

### 📝 blogs

| URL | View | Description |
|-----|------|-------------|
| `/blogs` | `index` | Placeholder — list all blogs |
| `/blogs/new` | `new` | Placeholder — form to create a new blog |
| `/blogs/create` | `create` | Redirects to `/blogs` |
| `/blogs/<number>` | `show` | Placeholder — display blog by number |
| `/blogs/<number>/edit` | `edit` | Placeholder — edit blog by number |
| `/blogs/<number>/delete` | `destroy` | Redirects to `/blogs` |

### 📋 surveys

| URL |  View | Description |
|-----|------|-------------|
| `/surveys` | `index` | Placeholder — list all surveys |
| `/surveys/new` | `new` | Placeholder — form to add a new survey |

### 👤 users

| URL | View | Description |
|-----|------|-------------|
| `/register` | `register` | Placeholder — create a new user record |
| `/login` | `login` | Placeholder — user login page |
| `/users/new` | `register` | Same view as `/register` |
| `/users` | `index` | Placeholder — list all users |

---

