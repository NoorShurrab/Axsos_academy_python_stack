# Great Number Game 
A Flask web application where the server picks a random number between 1 and 100 and stores it in the session. The user keeps guessing until they get it right — the server tells them if their guess is too high, too low, or correct.

## How to Run
1. Activate the environment:
    - flask_env\Scripts\activate

2. Install Flask:
    - pip install flask

3. Run the server:
    - python server.py

4. Access the route

## Routes
`[/]`                Picks a random number (first visit) and displays the guess form

`[/guess]`           Receives the user's guess and returns too high / too low / correct

`[/play_again]`      Clears the session and redirects to / for a new game

## How It Works 
1. User opens the page
   ↓
2. Server picks a random number and saves it in session
   session["number"] = random.randint(1, 100)
   ↓
3. User submits a guess
   ↓
4. Server compares the guess to session["number"]
   - guess < number  →  "Too low!"
   - guess > number  →  "Too high!"
   - guess == number →  "Correct!"
   ↓
5. User clicks Play Again → session is cleared → new number is picked
