# This file is the core of the application.
# It contains two routes:
# - "/" : Renders the main form page
# - "/result" : Receives form data via POST and renders the result page
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template("index.html", page_title = "Form")


@app.route("/result", methods=["POST"])
def result():
    name     = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment  = request.form.get("comment", "")

    return render_template("result.html", 
                            name=name, 
                            location=location, 
                            language=language, 
                            comment=comment , 
                            page_title = "Result"
    )


if __name__=="__main__":
    app.run(debug=True)