from BookSelector import BookSelector
from genres import genres
import pandas as pd
from textblob import TextBlob
#scrape multiple reviews from books. Use sentiment to pick most passionate reviews
#books = {"#": {'url': u, 'title': t, 'author': a, 'rating': r, 'synopsis': s, 'pageCount': p}, "Book #": {},...}

class ReviewScraper:
    def __init__(self,books,genre):
        self.books = books
        self.genre = genre
        self.reviews_df = pd.read_csv('Review_'+genres[self.genre]+'.csv',encoding='latin-1')
        self.reviews = {}
        self.chosen_reviews = {}
        self.scrap()
        self.choose()
        
    def scrap(self):
        count = 1
        for b in self.books:
            url = self.books[b]['url']
            df = self.reviews_df[url]
            self.reviews[str(count)]= df.tolist()
            count+=1
            

    def choose(self):
        for b in self.reviews:
            rev = self.reviews[b]
            chosen = str(rev[0])
            print(chosen)
            least_polarity = TextBlob(chosen).sentiment.polarity
            for x in rev:
                temp_pol = TextBlob(str(x)).sentiment.polarity
                if temp_pol<least_polarity:
                    least_polarity = temp_pol
                    chosen = str(x)
                self.chosen_reviews[b] = chosen    
