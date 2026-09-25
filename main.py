from flask import Flask, render_template, redirect, url_for, request as flask_request
from markupsafe import escape
import json
from xtramodules import isbn_fetcher, save_book_data
import urllib.request
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId


load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")



#Index Page
@app.route('/')
def index():
    #TODO:Make the username render here frfr
    username = "hyp-en"
    return render_template("index.html", username=username)

#lowk i made this to test stuff out , and I will NEVER remove stuff i tested unless explicitly mentioned so enjou
@app.route('/scrathpad')
def scratchpad():
    return render_template("scratchpad.html")

#Book Collection Page
@app.route('/collections')
def collection():
    return render_template("collections.html")

#Page count page
@app.route('/pgcount')
def pgcount():
    return render_template("pagecount.html")

#book adding
@app.route("/add-book", methods=["POST"])
def add_book_handler():
  isbn = flask_request.form.get("isbn")

  if isbn:
    new_book = save_book_data(isbn)
    if flask_request.headers.get("HX-Request"):
      return render_template("partials/book_card.html", book=new_book)

  return redirect(url_for("collection"))

#book moving
#TODO: lowk do this frfr

#TODO:Integrate Login and Usernames

#--- Uh Library ISBN Stuff ---#




#Runs the server without using the full command, running this file is enough
if __name__ == "__main__":
    app.run(debug=True)
