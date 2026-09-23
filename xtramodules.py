import json
from urllib import request

def isbn_fetcher(isbn):
    apiurl = f"https://openlibrary.org/isbn/{isbn}.json"

    req = request.Request(
        apiurl, 
        headers={'User-Agent': 'booKeeperApp/0.1 (educational project)'}
    )
    try:
        with request.urlopen(req) as response:
            book_meta = json.loads(response.read().decode('utf-8'))

        if book_meta:
            title = book_meta.get('title')
            authors = book_meta.get('authors', [])
            author_names = []

            if authors:
                for author in authors:
                    name = author.get('name')
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
                'cover': cover_url
            }

        else:
            return 'No Book Found!'
            
    except Exception as e:
        print(f"Oops! Something went wrong! Error: {e}")
        return 'No Book Found!'

if __name__ == "__main__":
    result = isbn_fetcher("9780143127741")
    print(result)