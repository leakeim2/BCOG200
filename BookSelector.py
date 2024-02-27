'''
NOTES:
- should rating threshold be set, or vary?
- return multiple books or just one? should the user get a pick
- should I give no synopsis, so the user only has the review?
- it would be fun to give the user five one star reviews of 5 books and they can pick based on that
- Goodreads API/database
- should I give them a pic of the book cover? idk covers are influential.
- if no preferences then pick whatever
- can the program learn?
- got API key for Google Books
'''

#pick 5 books??
#user can also not give genre if they don't want to
#filter for length??
#other types of filtering possibly --> research recommendation systems
class BookSelector:
    def __init__(self, user_genre=None):
        self.genre = user_genre
        self.min_rating = 4.00
