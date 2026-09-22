from flask import Flask, render_template, redirect, url_for
from markupsafe import escape

app=Flask(__name__)

#Index Page
@app.route('/')
def index():
    #TODO:Make the username render here frfr
    username = "Siddharth"
    return render_template("index.html", username=username)

#Book Collection Page
@app.route('/col')
def collection():
    return render_template("collections.html")

#Page count page
@app.route('/pgcount')
def pgcount():
    return render_template("pagecount.html")

#TODO:Integrate Login and Usernames



#Runs the server without using the full command, running this file is enough
if __name__ == "__main__":
    app.run(debug=True)
