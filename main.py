def main:
    while True:
        print("Hello. I will help you find a book. This book may be well regarded, but the consenus can be wrong and there are brutal reviews to prove it. ",
          "Lets get started.\n"
        print("Below is our list of genres that also have subgenres. You may browse the genres and once you click on a subgenre we will move on.")
          
        root = tk.Tk()
        b = Buttons(root)
        root.mainloop()
        user_genre = b.get_genre()
          
        user_options = input("Would you like options of books to choose from based on reviews? Enter Y/N")
        if user_options == 'N':
            user_options = False
        # other filters maybe
        # pass the info to Book Selector
        print("Sounds good. I'll take a look in the back and get you something to read")
        books = BookSelector(user_genre,user_options) # if they don't want options then this would be just one book
        reviews = ReviewScraper(books)

        stop = True
        while stop:
            sm_to_read = ReviewPresenter(reviews)
            # give the user sm_to_read
            # once they pick a review, give them the book that correlated to that review plus the synopsis and cover
            choice = input("Are you happy with your book? (yes/no)")
            if choice == 'yes':
                  break
            else:
                ans = input("Let's go back to the other options. If you would like to fully restart, enter 'yes'.")
                if ans == 'yes':
                    stop=False
        else:
            continue
        break
    
    print("okay yay now go read.")


if __name__ == __main__:
    main()
