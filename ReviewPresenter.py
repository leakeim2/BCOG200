# give the reader those reviews from which they will pick a book based on the review and then they get the name of the book
# books = {"Book#":{}}
# reviews = {"Book#": [{review},{review}]
# chosen_review = {"Book#": review}


class ReviewPresenter:
    def __init__(self, books, chosen_reviews):
        self.books = books
        self.chosen_reviews = chosen_reviews 
        self.go_forth_and_conquer()

    def go_forth_and_conquer(self):
        count = 1
        for x in range(5):
            key = "Book {}".format(x)
            if key in self.books:
                print(key + "Review: " + self.chosen_reviews[key]\n\n\n)
                count++
        if count==2:
            self.display_choice(1)
        else: 
            choice = input("Please enter a number 1-5 for your book selection.")
            self.display_choice(choice)


    def display_choice(self, count):
        key = "Book {}".format(count)
        print("Here is your Book...")
        print("\nTitle: "+ self.books[key[title]]) 
        print("Author: "+ self.books[key[author]])
        print("Synopsis: "+ self.books[key[synopsis]])
        print("Page Count: "+ self.books[key[pageCount]])
        #show picture???
        
