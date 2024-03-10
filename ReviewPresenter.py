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
        for x in range(5):
            if str(x) in self.books:
                self.display_review(str(x))
            else: 
                self.display_choice("1")
                break
        else: 
            x = input("Please enter a number 1-5 for your book selection.")
            self.display_choice(str(x))

    def display_review(self,key):
        print("Review",key,":",self.chosen_reviews[key['Review']])
        print("Reviewer:",self.chosen_reviews[key['Reviewer']])
        print("Date Published:", self.chosen_reviews[key['Date']])

    def display_choice(self,key):
        print("Here is your Book...\n")
        book = self.books[key]
        print("Title:", book['title']) 
        print("Author:", book['author'])
        print("Synopsis:", book['synopsis'])
        print("Page Count:", book['pageCount'])
        #show picture???
