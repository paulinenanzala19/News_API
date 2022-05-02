import unittest
from ..models import Article

class TestArticle(unittest.TestCase):

 def setUp(self):
    """

    """
    self.news_object=Article('null','Josef Fares doesnt think games need to be fun to suceed',
    'Josef Fares sat down with Rami Ismail for a GamesBeat Summit fireside chat to talk about passion drive and making games' 
    ,"https://venturebeat.com/2022/4/29/fares-doesnt-think-games-need-to-be-fun",
    'Erron Kelly','https://venturebeat.com/wp-content/uploads/2022/04/faresTGA.jpg?w=1200&strip=all','2022-04-29T17:30:00Z'
    )



 def test_instance():
    self.assertTrue(isinstance(self.news_object,Article))
 

if __name__ == "__main__":
    unittest.main()