# Champion Survey
A simple Flask web application that accepts a form submission and displays the submitted data on a results page.

## How to Run
1. Activate the environment:
    - flask_env\Scripts\activate

2. Install Flask:
    - pip install flask

3. Run the application:
    - python server.py

4. Access the routes

## Technologies Used
    Python
    Flask
    HTML / CSS
    Jinja (Flask templating engine)

## Features
1. Home page (/) — Displays a form with the following fields:
    - Name (text input)
    - Dojo Location (dropdown)
    - Favorite Language (dropdown)
    - Comment (optional textarea)

2. Result page (/result) — Displays the submitted form data
    - Go Back button — Returns the user to the home page