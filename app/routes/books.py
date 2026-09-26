from flask import Blueprint, render_template, redirect, url_for, request as flask_request

from app.services.books import save_book_data

books_bp = Blueprint("books", __name__)

@books_bp.route("/add-book", methods=["POST"])
def add_book_handler():
  isbn = flask_request.form.get("isbn")

  if isbn:  
    new_book = save_book_data(isbn)
    if flask_request.headers.get("HX-Request"):
      return render_template("partials/book_card.html", book=new_book)

  return redirect(url_for("collection"))