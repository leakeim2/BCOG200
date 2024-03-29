import tkinter as tk
from Buttons import Buttons
from BookSelector import BookSelector
from ReviewScraper import ReviewScraper
from ReviewPresenter import ReviewPresenter


class Main:
    def __init__(self,test=False,options=None,happy=None,back=None):
        self.op = options
        self.hap = happy
        self.back = back
        if test==False:
            self.run()
        else: self.runTest()

    def run(self):
        while True:
            print("Hello. I will help you find a book. This book may be well regarded, but the consenus can be wrong and there are brutal reviews to prove it. ",
                  "Lets get started.\n")
            print("Below is our list of genres that also have subgenres. You may browse the genres and once you click on a subgenre we will move on.")
          
            root = tk.Tk()
            b = Buttons(root)
            root.mainloop()
            genre = b.get_genre()
          
            self.op = input("Would you like options of books to choose from based on reviews? Enter Y/N")
            self.op = True if self.op.upper()=='Y' else False

            print("Sounds good. I'll take a look in the back and get you something to read")

            b = BookSelector(genre, self.op)
            books = b.books
            
            r = ReviewScraper(books)
            chosen_reviews = r.chosen_reviews

            stop = True
            while stop:
                something_to_read = ReviewPresenter(books, chosen_reviews)    
                self.hap = input("Are you happy with your book? (Y/N)")
                if self.hap.upper() == 'Y': break
                else:
                    self.back = input("Let's go back to the other options (K), or you can fully restart(Y)")
                    if self.back.upper() == 'Y':
                        stop=False
            else: continue
            break
    
        print("okay yay now go read.")

    def runTest(): 
        while True:
            self.op = True if self.op.upper()=='Y' else False
            
            b = BookSelector(fiction, self.op)
            books = b.books
            
            r = ReviewScraper(books)
            chosen_reviews = r.chosen_reviews

            stop = True
            while stop:
                something_to_read = ReviewPresenter(books, chosen_reviews)    
                if self.hap.upper() == 'Y': break
                else:
                    if self.back.upper() == 'Y':
                        stop=False
            else: continue
            break

if __name__ == "__main__":
    m = Main()
