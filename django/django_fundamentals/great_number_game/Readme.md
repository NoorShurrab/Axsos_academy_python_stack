# Great Number Game
A simple guessing game built with Django. The app picks a random number between 1 and 100, and the player has **5 attempts** to guess it correctly.

## How It Works
    - On first visit, a secret number (1–100) is generated and stored in the session.
    - The player submits guesses via a form.
    - After each guess, feedback is given: too low, too high, or correct.
    - The game ends when the player guesses correctly or exhausts all 5 attempts.
    - A "Play Again" and "Try Again" button resets the session and starts a new game.

## How to Run 
1. Activate the virtual environment:
    - django_env\Scripts\activate (Windows)

2. Create Django project
    - django-admin startproject great_number_game

3. Navigate into project
    - cd great_number_game
    
4. Create app
    - python manage.py startapp game_app
    
5. Run migrations
    - python manage.py makemigrations
    - python manage.py migrate

6. Run the server: 
    - python manage.py runserver

## Routes

| View | URL | Description |
|------|-----|-------------|
| `index` | `/` | Renders the game page; initializes session on first visit |
| `guess` | `/guess/` |  Handles guess submission and updates session state |
| `play_again` | `/play-again/` | Clears session and redirects to start a new game |


## Output 
