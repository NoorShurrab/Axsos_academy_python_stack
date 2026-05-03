# This code contains three routes:
# - "/"           : Picks a random number on first visit and displays the guess form
# - "/guess"      : Receives the user's guess via POST and returns too high / too low / correct
# - "/play_again" : Clears the session and redirects to "/" so the user can start a new game
from flask import Flask, render_template, request, redirect, session
import random

noor_app = Flask(__name__)
noor_app.secret_key = "anything"

@noor_app.route('/')
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0
    print(session["number"])
    return render_template('index.html', result=None)

@noor_app.route("/guess", methods=["POST"])
def guess():
    user_guess = int(request.form.get("guess"))
    number     = session["number"]
    if user_guess < number:
        result = "low"
    elif user_guess > number:
        result = "high"
    else:
        result = "correct"

    return render_template("index.html",
        result=result,
        guess=user_guess,
        secret=number,
    )

@noor_app.route("/play_again")
def play_again():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    noor_app.run(debug=True)