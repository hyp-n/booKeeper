import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from xtramodules import isbn_fetcher

load_dotenv()

bKpr = Flask(__name__)
bKpr.secret_key = os.getenv("SECRET_KEY")


@bKpr.route("/")
def index():
  return render_template("index.html", username="hyp-en")


@bKpr.route("/collections")
def collection():
  # TODO: Fetch collections from MongoDB and group by collection name
  return render_template("collections.html")


@bKpr.route("/add-book", methods=["POST"])
def add_book_handler():
  isbn = request.form.get("isbn")

  if not isbn:
    return "<p class='error'>ISBN is required</p>", 400

  # Save book using helper function
  new_book = isbn_fetcher(isbn)

  # HTMX Partial Swap: Return just the new book HTML card
  if request.headers.get("HX-Request"):
    return render_template("partials/book_card.html", book=new_book)

  return redirect(url_for("collection"))


@bKpr.route("/scrathpad")
def scratchpad():
  return render_template("scratchpad.html")


if __name__ == "__main__":
  bKpr.run(debug=True)