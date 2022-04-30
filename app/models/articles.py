class Article:
    """
    Article class to define article objects
    """

    def __init__(self, id,title,description,url,author,urlToImage):
        self.id=id
        self.title=title
        self.description=description
        # self.time=time
        self.url=url
        self.author=author
        self.urlToImage=urlToImage
       
    