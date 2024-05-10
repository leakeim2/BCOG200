#test file
#Description: Test, no user interaction. To use program instead of testing, use main.py
from main import Main
from BookSelector import BookSelector
from ReviewScraper import ReviewScraper
from ReviewPresenter import ReviewPresenter

#test BookSelector file. Check that the correct number of books exist within the books dicitonary.
def testBookSelector(b1,b2):
    failed = False
    if len(b1.books)== 5 and len(b2.books) == 1:
        for x in b1.books:
            if (x not in ['1','2','3','4','5'] or
            b1.books[x]['url'] == None or
            b1.books[x]['title'] == None or
            b1.books[x]['author'] == None or
            b1.books[x]['rating'] < 4.00 or
            b1.books[x]['pageCount'] < 100 or
            b1.books[x]['synopsis'] == None):
                failed = True
            if '1' not in b2.books: failed = True
    if failed == False: return("Book Selector Testing is Complete")
    raise AssertionError('BookSelector test failed')

#test ReviewScraper file. Check that number of reviews matches to books, and that they exist.
def testReviewScraper(r):
    # will need to test that a sufficient review is collected for each book, for different selections of books
    failed = False
    if len(r.reviews) != 5: failed = True
    for x in r.reviews:
        for w in r.reviews[x]:
            if w==None: failed = True
    if len(r.chosen_reviews) !=5: failed = True
    for x in r.chosen_reviews:
        if r.chosen_reviews[x] == None: failed = True
    if failed == False: return("Review Scraper Testing is Complete")
    raise AssertionError('ReviewScraper test failed')

#test main file. Check that user instructions leads to the right pathway.
def testMain():
    m = Main(True,'Y','Y')
    if m.result == 'happy':
        m = Main(True,'Y','N')
        if m.result == 'happy':
            m = Main(True,'N','Y')
            if m.result == 'back':
                m = Main(True,'N','N')
                if m.result == 'revisit':
                    m = Main(True,'t','N')
                    if m.result == 'typo':
                        m = Main(True,'N','p')
                        if m.result == 'typo':
                            return ("Main Testing is Complete")
    raise AssertionError('main test failed')

if __name__ == "__main__":
    b1 = BookSelector('No Preference')
    b2 = BookSelector('No Preference',False)
    r = ReviewScraper(b1.books,'No Preference')
    print(testBookSelector(b1,b2))
    print(testReviewScraper(r))
    print(testMain())
    print("\nYay your code works;)")
