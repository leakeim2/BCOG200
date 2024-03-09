import tkinter as tk
from Buttons import Buttons
from BookSelector import BookSelector
from ReviewScraper import ReviewScraper
from ReviewPresenter import ReviewPresenter


def main():
    while True:
        print("Hello. I will help you find a book. This book may be well regarded, but the consenus can be wrong and there are brutal reviews to prove it. ",
          "Lets get started.\n")
        print("Below is our list of genres that also have subgenres. You may browse the genres and once you click on a subgenre we will move on.")
          
        root = tk.Tk()
        b = Buttons(root)
        root.mainloop()
        genre = b.get_genre()
          
        options = input("Would you like options of books to choose from based on reviews? Enter Y/N")
        options = True if options.upper()=='N' else False
        print("Sounds good. I'll take a look in the back and get you something to read")
        b = BookSelector(genre, options)
        books = b.books
        r = ReviewScraper(books)
        chosen_reviews = r.chosen_reviews

        stop = True
        while stop:
            something_to_read = ReviewPresenter(books, chosen_reviews)
            choice = input("Are you happy with your book? (Y/N)")
            if choice.upper() == 'Y': break
            else:
                ans = input("Let's go back to the other options (K), or you can fully restart(Y)")
                if ans.upper() == 'Y':
                    stop=False
        else: continue
        break
    print("okay yay now go read.")


if __name__ == "__main__":
    main()
