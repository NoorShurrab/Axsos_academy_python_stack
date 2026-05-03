# This code manages a visit counter using
# Flask session to persist data across requests
from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "any_secret_key"  # Required to encrypt the session cookie

# Root route — displays the counter and increments it on each visit
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html", count=session["count"], page_title = "Counter")
    

# Add two route — increments the counter by 2
@app.route("/add_two")
def add_two():
    session["count"] += 2
    return render_template("index.html", count=session["count"])

# Reset route — resets the counter to 0 without clearing the session
@app.route("/reset")
def reset():
    session["count"] = 0
    return render_template("index.html", count=session["count"])


# Destroy session route — clears the entire session and redirects to root
@app.route("/destroy_session")
def destroy_session():
    session.clear()     
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)