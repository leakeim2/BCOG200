import requests
from genres import genres
import pandas as pd

class BookSelector:
    def __init__(self, genre, options=True):
        self.genre = genre
        self.books_df = pd.read_csv(genres[self.genre]+'.csv',encoding='latin-1')
        self.numBooks = 5
        if not options: self.numBooks = 1
        self.books = {}
        self.fetch(self.numBooks)

    def fetch(self,n):
        self.books_df['rating']= pd.to_numeric(self.books_df['rating'],errors='coerce')
        df = self.books_df.dropna(subset=['rating'])
        df = df[df['rating']>= 4.00]
        random_books = df.sample(n=n,replace=False)
        count = 1
        for i, row in random_books.iterrows():
            title = row['title']
            url = row['url']
            author = row['author']
            rating = row['rating']
            pageCount = row['pageCount']
            synopsis = row['synopsis']
            self.books[str(count)]={'url': url,
                                  'title': title,
                                  'author': author,
                                  'rating': rating,
                                  'synopsis':synopsis,
                                  'pageCount': pageCount}
            count+=1

