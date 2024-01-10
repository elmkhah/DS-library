from _database import*
from user import*

class book:
    def __init__(self,title=None,content=None,publication_year=None,writer=None):
        self.ID=-1
        self.title=title
        self.content=content
        self.publication_year=publication_year
        self.writer=writer
        
    def add_book(book_list):
        #input data
        temp_book=book()
        temp_book.title=input("book title: ")
        temp_book.content=input("content: ")
        temp_book.publication_year=input("publication year: ")
        temp_book.writer=input("writer: ")

        # check ID in linked list
        current_node = book_list.head
        while current_node:
            if current_node.data.title == temp_book.title:
                print("Duplicate book found")
                break
            current_node = current_node.next    
        book_list.insert_first(temp_book)
        print("book successfully added!")
        return temp_book   # return current book
    