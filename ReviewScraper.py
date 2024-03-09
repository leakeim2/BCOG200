import requests
#scrape multiple reviews from books --> can I somehow pick the longest reviews?
#books = {"Book #": {'id': i, 'title': t, 'author': a, 'rating': r, 'synopsis': s, 'pageCount': p}, "Book #": {},...}

API_KEY = 'AIzaSyBPRZp5uuPc2Sp0rpIQzZofSJDmGcWv7Q8'
url = 'https://www.googleapis.com/books/v1/volumes/'

class ReviewScraper:
    def __init__(self,books):
        self.books = books
        self.params = {'key': API_KEY}
        self.reviews = {}
        self.chosen_reviews = {}
        self.scrap()
        self.choose()
        
    def scrap(self):
        for b in books:
            reviews[b] = []
            response = requests.get(url+books[b['id']],params=params)
            if response.status_code == 200:
                data = response.json()
                review_data = data.get('volumeInfo',{}).get('reviews',[])
                for r in review_data:
                    rating = r.get('rating')
                    if rating and int(rating) ==1:
                        content = r.get('content','No review text')
                        reviewer = r.get('author',{}).get('displayName','Anonymous')
                        date = r.get('published','Unknown')
                        reviews[b].append({'Review': content, 'Reviewer': reviewer,'Date': date})
            else:
                print('Error:', response.status_code)

    def choose(self):
        for b in self.reviews:
            list = self.reviews[b]
            if len(list)==0:
                self.chosen_reviews[b] = None 
            else:
                for x in list:
                    #go through reviews
                    #now I have all the reviews for this book. Idk how I will pick one out just yet
                chosen_review = {one of the reviews} 
                self.chosen_reviews[b] = chosen_review
            
            
