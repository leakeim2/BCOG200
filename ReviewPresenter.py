# give the reader those reviews from which they will pick a book based on the review and then they get the book information
# books = {"1":{}}
# reviews = {"1": [{review},{review}]
# chosen_review = {"1": review}

class ReviewPresenter:
    def __init__(self, books, chosen_reviews):
        self.books = books
        self.chosen_reviews = chosen_reviews 
        self.go_forth_and_conquer()

    #go through each review and call display_review
    #then display the review corresponding to the user's input
    def go_forth_and_conquer(self):
        for b in self.books:
            self.display_review(b)
        if len(self.books)>1:
            x = input("\nPlease enter a number 1-5 for your book selection.")
        else: x = 1
        self.display_choice(str(x))

    #show the review to the reader with a label
    def display_review(self,key):
        print("REVIEW",key+":")
        print(self.chosen_reviews[key],'\n')

    #show all the book information
    def display_choice(self,key):
        print("\nHere is your Book...\n")
        book = self.books[key]
        print("TITLE:", book['title']) 
        print("AUTHOR:", book['author'])
        print("SYNOPSIS:", book['synopsis'])
        print("PAGE COUNT:", book['pageCount'])
