import unittest
from app.models import Article

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
 
 def test_init(self):
    self.assertEqual(self.new_object.id,'null')
    self.assertEqual(self.new_object.title,'Josef Fares doesnt think games need to be fun to suceed')
    self.assertEqual(self.new_object.description,'Josef Fares sat down with Rami Ismail for a GamesBeat Summit fireside chat to talk about passion drive and making games')
    self.assertEqual(self.new_object.url,'https://venturebeat.com/2022/4/29/fares-doesnt-think-games-need-to-be-fun')
    self.assertEqual(self.new_object.author,'Erron Kelly')
    self.assertEqual(self.new_.object.urlToImage,'https://venturebeat.com/wp-content/uploads/2022/04/faresTGA.jpg?w=1200&strip=all')
    self.assertEqual(self.new_object.publishedAt,'2022-04-29T17:30:00Z')
