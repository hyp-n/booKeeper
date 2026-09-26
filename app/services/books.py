from .openlibrary import isbn_fetcher
import pymongo
import os
from pymongo.errors import DuplicateKeyError
from dotenv import load_dotenv
import time

load_dotenv()

def save_book_data(isbn):
    start = time.time()
    book_data = isbn_fetcher(isbn)
    print(f"OL: {time.time()-start}")
    if isinstance(book_data, dict):
        start = time.time()
        myclient = pymongo.MongoClient(os.getenv("MONGO_URI"))
        mydb = myclient["mydatabase"] 
        total_books = mydb["all_books"]   
        try:
            result = total_books.insert_one(book_data)
        except DuplicateKeyError:
            return False
        book_data["_id"] = result.inserted_id
        print(f"MDB: {time.time() - start}")  
        return book_data
    return False

def get_books_collection():
    client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    books = client["mydatabase"]["all_books"]
    return books

def get_collections():
    books_col = get_books_collection()
    collections = {}

    for i in books_col.find().sort("title", 1):  
        folder = i.get("collection") or "UNCOLLECTED"  
        collections.setdefault(folder, []).append(i)
 
    return collections




