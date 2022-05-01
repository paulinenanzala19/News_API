class Article:
    """
    Article class to define article objects
    """

    def __init__(self, id,title,description,url,author,urlToImage,publishedAt):
        self.id=id
        self.title=title
        self.description=description
        self.url=url
        self.author=author
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt

class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,description,publishedAt,url,urlToImage,title):
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        self.title = title
       
    