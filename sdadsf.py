class Book:
    def __init__(self,isbn):
        self.isbn = isbn
        isbn = 'test'


book = Book(12345)
print(book.isbn)