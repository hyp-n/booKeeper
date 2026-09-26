import os
from flask import Flask
from dotenv import load_dotenv
from app.routes.books import books_bp
from app.routes.collections import collections_bp
from app.routes.pages import pages_bp

def create_app():
    load_dotenv()
    app=Flask(__name__)
    
    app.register_blueprint(books_bp)
    app.register_blueprint(collections_bp)
    app.register_blueprint(pages_bp)

    return app