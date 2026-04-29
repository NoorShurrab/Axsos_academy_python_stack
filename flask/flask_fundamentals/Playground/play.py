# "This code implements a dynamic playground page by merging three routes into one efficient function. 
# It passes user-defined or default values for count and color to a Jinja template."
from flask import Flask, render_template
noor_app = Flask(__name__)

@noor_app.route('/play')
@noor_app.route('/play/<int:num>')
@noor_app.route('/play/<int:num>/<string:color>')
def playground(num=3, color="lightblue"):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    noor_app.run(debug=True)

