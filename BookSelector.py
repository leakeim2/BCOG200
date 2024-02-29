import requests

API_KEY = 'AIzaSyBPRZp5uuPc2Sp0rpIQzZofSJDmGcWv7Q8'
url = "https://www.googleapis.com/books/v1/volumes"

class BookSelector:
    def __init__(self, user_genre=None, user_options = True):
        self.genre = user_genre
        self.numBooks = 5
        if not user_options: self.numBooks = 1
        self.books = {}
        self.search_params = {'q': 'subject:'+self.genre, 'maxResults':20}
        self.params = {'q':'+'.join([f"{key}:{value}" for key, value in search_params.items() if value is not None]), 'key': API_KEY}
        self.fetch(self.numBooks)

    def fetch(self,n):
        while len(self.books)<n:
            response = requests.get(url,params=params)
            if response.status_code == 200:
                data = response.json()
                for 'items' in data and len(data['items'])>0:
                    for item in data['items']:
                        if 'averageRating' in item['volumeInfo']:
                            rating = item['volumeInfo']['averageRating']
                            ratingNum = item['volumeInfo']['ratingsCount']
                            if rating>= 4.00 and ratingNum>500:
                                title = item['volumeInfo]['title']
                                author = item['volumeInfo]['authors'] if 'authors' in item['volumeInfo' else[Unknown']
                                synopsis = item['volumeInfo]['description']
                                pageCount = item['volumeInfo']['pageCount']
                                books.append({title: author, rating, synopsis, pageCount})
                                if len(books) == n: break
                    else:
                        if 'nextPageToken' in data:
                            params['pageToken'] = data['nextPageToken']
                        else: break
                else: break
            else: 
                print("Error:", response.status_code)
                break


