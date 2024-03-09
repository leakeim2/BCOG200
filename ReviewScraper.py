#scrape multiple reviews from books --> can I somehow pick the longest reviews?
#books = [{'id': i, 'title': t, 'author': a, 'rating': r, 'synopsis': s, 'pageCount': p}, {}]

API_KEY = 'AIzaSyBPRZp5uuPc2Sp0rpIQzZofSJDmGcWv7Q8'
url = 'https://www.googleapis.com/books/v1/volumes/'

class ReviewScraper:
    def __init__(self,books):
        self.books = books
        self.params = {'key': API_KEY}
        reviews = {}
        
    def scrap(self):
        for b in books:
            response = requests.get(url+b['id'],params=params
            if response.status_code == 200:
                data = response.json()
                review_data = data.get('volumeInfo',{}).get('reviews',[])
                for r in review_data:
                    rating = r.get('rating')
                    if rating and int(rating) ==1:
                        content = r.get('content','No review text')
                        reviewer = r.get('author',{}).get('displayName','Anonymous')
                        date = r.get('published','Unknown')
                        reviews[b]={'Review': content, 'Reviewer':reviewer,'Date':date})
                    if b not in reviews:
                        reviews.append(b: "Perhaps sometimes the consensus is objective. There are no one star reviews. If a book has no passionate haters then the book is not worth reading but do as you will")
            
            else:
                print('Error:', response.status_code)

            
            
