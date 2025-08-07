class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_checked_out="no"
        return boo



class Library(Book):
    def __init__(self):
        self.title=""
        self.author=""
        bk=Book(self.title,self.author)
        self.__book=[Book(self.title,self.author)]
        self.__checked_out=[Book(self.title,self.author)]
       

#    def setup(self):
#        self.bk=book()
        
    def add_book(self,bk):
        self.__book.append(bk)

    def check_out_book(self,title):
        for book in self.__book:
            if book.title==title:
                self.__checked_out.append(book)
                self.__book.remove(book)
                True
        
       

    def return_book(self,title):
        for book in self.__checked_out:
            if book.title==title:
                 self.__book.append(book)
       

    def list_available_books(self):
        for self.book in self.__book:
            print(f"{self.book.title}, {self.book.author}")
   #     print( f"{self.__book}")
    
