#Description: This is what the user may run to test the program. It will cover all combinations the program is expected to run which includes testing the classes 
# individually, and then testing the main file to ensure that user interaction runs smoothly. 
import unittest
from Main import Main
from Buttons import Buttons
from BookSelector import BookSelector
from ReviewScraper import ReviewScraper
from ReviewPresenter import ReviewPresenter


class Test(unittest.TestCase):
  def testButtons(self):
    # will need to include selection of...
    # genre and subgenre
    # genre and no preference
    # no preference
    # will also need to test that the back button works
    print("Buttons Testing is Complete")

  def testBookSelector(self):
    # will need to test search for multiple genres as well as no preference
    print("Book Selector Testing is Complete")

  def testReviewScraper(self):
    # will need to test that a sufficient review is collected for each book, for different selections of books
    print("Review Scraper Testing is Complete")

  def testReviewPresenter(self):
    # will need to test that the reviews and book information is displayed properly and that the user instruction works properly
    print("Review Presenter Testing is Complete")

  def testMain(self):
    # will need to test that front end of the code works with the user and test all user responses...
    # all combinations of the choices presented
    # ensure that the code accomodates for user error such as invalid responses and uppercase vs lowercase
    # we will run Main with the choices preselected ie. m = Main(True, False, True)
    print("Main Testing is Complete")
    

if __name__ == "__main__":
  unittest.main()
  print("\nYay your code works;)")

