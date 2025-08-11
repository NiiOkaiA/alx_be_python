class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

class EBook(Book):
    def __init__(self,file_size):
        super().__init__(Book)
        self.file_size=file_size

class PrintBook(Book):
    def __init_(self,page_count):
        super().__init__(Book)
        self.page_count=page_count

class Library:
     # def __init__(self,book):
     #     self.book=book

      def add_book(self,book):
          self.book=book
          book_list.append(book)


      def list_books(self):
          print(book_list)

    


