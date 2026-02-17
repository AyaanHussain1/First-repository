# static is folder which holds all the public files (you can only put files in static which you want to show in public - not confidential)
# You’re right: in a normal script, a function sits idle until you explicitly type hello_world().In Flask, the framework handles the calling for you. This is a concept called Inversion of Control.
from flask import Flask,render_template # import render template to run template of html

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template("index.html")
app.run(debug=True)
 