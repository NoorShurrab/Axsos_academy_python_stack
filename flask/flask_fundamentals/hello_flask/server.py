# This is a simple Flask web application that defines several routes to handle different types of requests.
from flask import Flask
app = Flask(__name__)

# This function handles requests to the main page (localhost:5000/).
@app.route('/')
def hello():
    return "Hello, World!"

# This function triggers when the user visits localhost:5000/Champion.
@app.route('/Champion')
def champion():
    return "Champion!"

# This function takes a string 'name' from the URL and returns a personalized greeting.
@app.route('/say/<name>')
def say_hello(name):
    return f"Hi, {name}!"

# This function accepts an integer 'num' and a string 'word'. 
# It repeats the word 'num' times as HTML paragraphs.
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    output = ""
    for i in range(num):
        output += f"<p>{word}</p>"
    return output

if __name__ == "__main__":
    app.run(debug=True)
