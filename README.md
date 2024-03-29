DOCUMENTATION FILE:
- User will be prompted with a description of the program and then they will select some preferences for their book search including a genre, and some other specifications
- The program will collect a dictionary of 5 books through Book Selector Module
- The program will pass the dictionary to the Review Scraper Module and collect 5 one-star reviews for each book
- The program will then pass the review dictionary to the Review Presenter Module which will show the user the reviews. Then the user will be able to select a review and see the book it is correlated with
- If the user is unhappy with their book, they may go back to the other 4 reviews they were given that correlate to 4 different books, or they may begin the program all over again.
- This is an explanation for the main.py file which includes the program condensed and the statements that the user will read and respond to.


BCOG 200 Project

Title: "Bad Reviews(Perchance)"

1) The project idea is partially based on a book generator function. The program will only give the user the most horrid 1-star reviews of books that are rated quite highly. The user theoretically doesn't know the books popularity or rating and the rating is useless anyways because I just read the most terrible, ill written book I have come across in a while, and it was given over 4.2 starts on good reads. The user can choose to read the book or not(or choose from multiple books) based on the review, but the concept is that since they've read the lowest opinion of said book and cannot see anything else, they will enjoy it more than they would otherwise, unless the book is as horrid as the review claimed which is not unlikely. At least at that point disaster was among expectations.
2)
* Develop a function that selects highly-rated books from a dataset (e.g., from Google Books API) based on user preferences, filtering for books with average ratings above a certain threshold.--> pick 5 books maybe. Possibly filter for long and short reads. Other types of filtering?
  
* Utilize a web scraping library like BeautifulSoup to extract 1-star reviews for the selected books from Google books or other review platforms.---> scrape multiple reviews from books, can I somehow pick the longest review, or analyze reviews to find more passionate ones?
  
* Implement a function to present a random 1-star review to the user for each recommended book, potentially highlighting exaggerated or humorous criticisms. Maybe also present a list of adjectives that are used to describe said book throughout reviews.--> the user can decide what to read by choosing one of the reviews?

   *If the user choses to read and complete the book they will still not be able to see any other reviews because it is important for people to trust their own opinions without relying on others. It is okay to like a terrible book and this program ensures that our users are not pressured by any positive feedback. Negative feedback is welcomed of course because hatred fuels the enemy of bad writing and no plot.
