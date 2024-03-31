from Buttons import createButtons
from BookSelector import BookSelector
from ReviewScraper import ReviewScraper
from ReviewPresenter import ReviewPresenter


class Main:
    def __init__(self,test=False,happy=None,back=None):
        self.op = None
        self.hap = happy
        self.back = back
        if test==False:
            self.run()
        else: self.runTest()

    def run(self):
        while True:
            print("Hello. I will help you find a book. This book may be well regarded, but the consenus can be wrong and there are brutal reviews to prove it. ",
                  "Lets get started.\n")
            print("Below is our list of genres from which you may choose.")
          
            genre = createButtons()
          
            self.op = input("Would you like options of books to choose from based on reviews? Enter Y/N")
            while (self.op.upper() != ('Y' and 'N')):
                self.op = input("That is not Y nor N, please enter Y/N")
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
                while (self.hap.upper() != ('Y' and 'N')):
                    self.hap = input("That is not Y nor N, please enter Y/N")
                if self.hap.upper() == 'Y': break
                else:
                    self.back = input("Let's go back to the other options (Y), or you can fully restart(N)")
                    while (self.back.upper() != ('Y' and 'N')):
                        self.back = input("That is not Y nor N, please enter Y/N")
                    if self.back.upper() == 'Y':
                        stop=False
            else: continue
            break
    
        print("okay yay now go read.")

    #still work in progress
    def runTest(): 
        while True:
            stop = True
            while stop:   
                if self.hap.upper() != ('Y' and 'N'): return "typo"
                if self.hap.upper() == 'Y': break
                elif self.back.upper() != ('Y' and 'N'): return "typo"
                elif self.back.upper() == 'Y':
                    stop=False
                return "revisit"
            else: 
                return "back"
            return "happy"

if __name__ == "__main__":
    m = Main()
