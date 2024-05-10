# give the reader those reviews from which they will pick a book based on the review and then they get the name of the book
# books = {"1":{}}
# reviews = {"1": [{review},{review}]
# chosen_review = {"1": review}


class ReviewPresenter:
    def __init__(self, books, chosen_reviews):
        self.books = books
        self.chosen_reviews = chosen_reviews 
        self.go_forth_and_conquer()

    def go_forth_and_conquer(self):
        for b in self.books:
            self.display_review(b)
        x = input("\nPlease enter a number 1-5 for your book selection.")
        self.display_choice(str(x))

    def display_review(self,key):
        print("REVIEW",key+":")
        print(self.chosen_reviews[key],'\n')

    def display_choice(self,key):
        print("\nHere is your Book...\n")
        book = self.books[key]
        print("TITLE:", book['title']) 
        print("AUTHOR:", book['author'])
        print("SYNOPSIS:", book['synopsis'])
        print("PAGE COUNT:", book['pageCount'])
