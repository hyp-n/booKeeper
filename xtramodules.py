import json
import urllib.request
import pymongo
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from flask import render_template, request

load_dotenv()

def isbn_fetcher(isbn):
    apiurl = f"https://openlibrary.org/isbn/{isbn}.json"

    req = urllib.request.Request(
        apiurl, 
        headers={'User-Agent': 'booKeeperApp/0.1 (educational project)'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            book_meta = json.loads(response.read().decode('utf-8'))

        if book_meta:
            title = book_meta.get('title')
            authors = book_meta.get('authors', [])
            author_names = []

            if authors:
                for author in authors:
                    name = author.get('key')
                    if name:
                        author_names.append(name)
                    else:
                        author_names.append(str(author.get('key', 'Unknown Author')))

            covers = book_meta.get('covers', [])
            if covers:
                cover_url = f"https://covers.openlibrary.org/b/id/{covers[0]}-M.jpg"
            else:
                cover_url = None

            return {
                'title': title,
                'authors': author_names,
                'cover': cover_url,
                'isbn': isbn.replace("-", "").replace(" ", "")
            }

            

        else:
            return 'No Book Found!'
        

    except Exception as e:
        print(f"Oops! Something went wrong! Error: {e}")
        return 'No Book Found!'

def save_book_data(isbn):
    book_data = isbn_fetcher(isbn)
    if isinstance(book_data, dict):
        myclient = pymongo.MongoClient(os.getenv("MONGO_URI"))
        mydb = myclient["mydatabase"] 
        total_books = mydb["all_books"]   
        total_books.insert_one(book_data)
        return True
    return False

def get_books_collection():
    client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    return client["mydatabase"]["all_books"]

def get_collections():
    books_col = get_books_collection()
    collections = {}

    for i in books_col.find().sort("title", 1):  
        folder = i.get("collection") or "UNCOLLECTED"  
        collections.setdefault(folder, []).append(i)
 
    return collections

# Added libgen to collections.html instead of the other sources lmao



