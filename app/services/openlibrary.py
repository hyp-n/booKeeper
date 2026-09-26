import json
import urllib.request
import time

def isbn_fetcher(isbn):
    apiurl = f"https://openlibrary.org/isbn/{isbn}.json"

    req = urllib.request.Request(
        apiurl, 
        headers={'User-Agent': 'booKeeperApp/0.1 (educational project)'}
    )
    try:
        start = time.time()

        with urllib.request.urlopen(req) as response:
            print("OL connection/response:", time.time() - start)
            book_meta = json.loads(response.read().decode('utf-8'))
            print("OL total:", time.time() - start)

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