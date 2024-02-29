#scrape multiple reviews from books --> can I somehow pick the longest reviews?
#books = [{'id': i, 'title': t, 'author': a, 'rating': r, 'synopsis': s, 'pageCount': p}, {}]

API_KEY = 'AIzaSyBPRZp5uuPc2Sp0rpIQzZofSJDmGcWv7Q8'
url = f'https://www.googleapis.com/books/v1/volumes/'

class ReviewScraper:
    def __init__(self,books):
        self.books = books
        self.params = {'key': API_KEY}
        
    def scrap(self):
        for b in books:
            response = requests.get(url+b['id'],params=params
            if response.status_code == 200:
                data = response.json()
            
            else:
                print('Error:', response.status_code)

            
            
