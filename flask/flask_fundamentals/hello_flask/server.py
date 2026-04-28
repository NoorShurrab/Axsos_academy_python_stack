from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/Champion')
def champion():
    return "Champion!"

@app.route('/say/<name>')
def say_hello(name):
    return f"Hi, {name}!"

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    output = ""
    for i in range(num):
        output += f"<p>{word}</p>"
    return output

if __name__ == "__main__":
    app.run(debug=True)
