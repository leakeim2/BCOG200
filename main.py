def main:
    print("Hello. I will help you find a book. This book may be well regarded, but the consenus can be wrong and there are brutal reviews to prove it ",
          "These books are popular, however sometimes people are wrong and have no taste. Lets get started.\n"
    print("Below is our list of genres that also have subgenres. You may click on a genre and then select a subgenre.")
    print(genres.keys)
          #register what they click as genre
    print(genres[key])
          #register what they click as subgenre
    user_genre = (genre, subgenre)
    #if user genre is empty then don't pass anything into Book Selector
    print("Would you like options of books to choose from based on reviews? Enter Y/N")
    # register input
    # if they enter 'N', then pass False in parameter for user_options, otherwise pass nothing

    # do this same format for other filters if I do those, and then pass all the preferences ito Book Selector
    print("Sounds good. I'll look in the back and get you something to read")

    books = BookSelector(parameters) # if they don't want options then this would be just one book
    reviews = ReviewScraper(books)
    sm_to_read = ReviewPresenter(reviews)
    # give the user sm_to_read
    # once they pick a review, give them the book that correlated to that review plus the synopsis and cover
    # Need a function to go back to the options if they want to pick a different one. And a function to start all over again.
    print("Are you happy with your book? Enter 'B' to go back to the other book options and 'R' to restart the selection.")

    

if __name__ == __main__:
    main()
