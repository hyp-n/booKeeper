from flask import Blueprint, render_template, redirect, url_for, request as flask_request

pages_bp = Blueprint("pages", __name__)

@pages_bp.route('/')
def index():
    #TODO:Make the username render here frfr
    username = "hyp-en"
    return render_template("index.html", username=username)


@pages_bp.route('/scrathpad')
def scratchpad():
    return render_template("scratchpad.html")


@pages_bp.route('/pgcount')
def pgcount():
    return render_template("pagecount.html")
