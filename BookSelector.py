import requests

API_KEY = 'AIzaSyBPRZp5uuPc2Sp0rpIQzZofSJDmGcWv7Q8'
url = "https://www.googleapis.com/books/v1/volumes"

class BookSelector:
    def __init__(self, user_genre, user_options):
        self.genre = user_genre
        self.numBooks = 5
        if not user_options: self.numBooks = 1
        self.books = {}
        self.params = {'q': f'subject:{self.genre}',
                       'maxResults': 20,
                       'key': API_KEY}
        self.fetch(self.numBooks)

    def fetch(self,n):
        while len(self.books)<n:
            response = requests.get(url,params=params)
            if response.status_code == 200:
                data = response.json()
                count=1
                if len(data['items'])>0:
                    for item in data['items']:
                        if 'averageRating' in item['volumeInfo']:
                            rating = item['volumeInfo']['averageRating']
                            ratingNum = item['volumeInfo']['ratingsCount']
                            if rating>= 4.00 and ratingNum>500:
                                title = item['volumeInfo']['title']
                                author = item['volumeInfo']['authors'] if 'authors' in item['volumeInfo'] else['Unknown']
                                synopsis = item['volumeInfo']['description']
                                pageCount = item['volumeInfo']['pageCount']
                                id = item['id']
                                self.books[str(count)]={'id': id,'title': title,'author': author,'rating': rating,'synopsis':synopsis,'pageCount': pageCount}
                                count+=1
                                if len(self.books) == n: break
                    else:
                        if 'nextPageToken' in data:
                            params['pageToken'] = data['nextPageToken']
                        else: break
                else: break
            else: 
                print("Error:", response.status_code)
                break


