#scrape multiple reviews from books --> can I somehow pick the longest reviews?
#books = {{title: volumeId, author, rating, synopsis, pageCount}, {}}

API_KEY = 'AIzaSyBPRZp5uuPc2Sp0rpIQzZofSJDmGcWv7Q8'
url = 'https://www.googleapis.com/books/v1/volumes/{volumeId}'

class ReviewScraper:
    def __init__(self,books):
        self.Id = books[
