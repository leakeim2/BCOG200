import requests
from genres import genres

class BookSelector:
    def __init__(self, genre, options=True):
        self.url = "https://biblioreads.eu.org/list/show/"
        self.genre = genre
        self.numBooks = 5
        if not options: self.numBooks = 1
        self.books = {}
        self.url += genres[self.genre]
        self.fetch(self.numBooks)

    def fetch(self,n):
        count = 1
        while len(self.books)<n:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return data
                for item in data:
                    title = 
                    author = 
                    synopsis = 
                    pageCount = 
                    self.books[str(count)]={'id': id,'title': title,'author': author,'rating': rating,'synopsis':synopsis,'pageCount': pageCount}
                    count+=1
                    if len(self.books) == n:
                        break
                if 'nextPageToken' in data:
                    self.params['pageToken'] = data['nextPageToken']
                else: break
            else:
                print("Error:", response.status_code)
                break

