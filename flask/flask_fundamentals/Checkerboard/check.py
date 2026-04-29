# This code defines flexible routes to render a grid with default (8x8) or custom dimensions (x, y).
# Passes dynamic coordinates to the template to build the grid based on row and column parity.
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", x = 8, y = 8)
@app.route('/<int:x>')
def row_count(x):
    return render_template("index.html", x = x, y = 8)
@app.route('/<int:x>/<int:y>')
def custom_grid(x, y):
    return render_template("index.html", x =x, y=y)

if __name__ == "__main__":
    app.run(debug=True)