from flask import Blueprint, render_template, redirect, url_for, request as flask_request

from app.services.books import get_collections

#so, in blueprint is lowk easier than the old shit
collections_bp = Blueprint("books",__name__)

@collections_bp.route('/collections')
def collection():
    collections = get_collections()
    return render_template("collections.html", collections= collections)
