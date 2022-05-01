import unittest
from ..models import Source

class TestSource(unittest.TestCase):
    def setUp(self):
        self.sources=Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at"
        "https://abcnews.go.com")