import _database
class Book:
    def __init__(self,title,content,publication_year,writer):
        self.ID=_database.last_ID("books")
        self.title=title
        self.content=content
        self.publication_year=publication_year
        self.writer=writer
        