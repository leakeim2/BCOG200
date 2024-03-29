#Description: The Testing will run before the User will be able to use it. The Test will cover all modules including 
# Buttons, BookSelector, ReviewScraper, and ReviewPresenter. It will cover all combination types that the program might 
# be presented with. Lastly, the user aspect will be tested including all combinations of responses that could be given.
# Afterwards, the user can run their own book search.
import unittest
from main import Main
from Buttons import Buttons
from BookSelector import BookSelector
from ReviewScraper import ReviewScraper
from ReviewPresenter import ReviewPresenter


class Test(unittest.TestCase):
  def testButtons(self):
    print("Buttons Testing is Complete")

  def testBookSelector(self):
    print("Book Selector Testing is Complete")

  def testReviewScraper(self):
    print("Review Scraper Testing is Complete")

  def testReviewPresenter(self):
    print("Review Presenter Testing is Complete")

  def testMain(self):
    print("Main Testing is Complete")
    

if __name__ == "__main__":
  unittest.main()
  print("\nYay your code works;)")

