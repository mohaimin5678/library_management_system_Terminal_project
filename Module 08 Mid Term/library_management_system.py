class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability

    @property
    def book_id(self):
        return self.__book_id
    
    def borrow_book(self):
        if self.__availability==True:
            self.__availability=False
            return f"Book '{self.__title}' borrowed successfully."
        else:
            return f"Book '{self.__title}' is already borrowed. Wait for the return"
    
    def return_book(self):
        if self.__availability==False:
            self.__availability=True
            return f"Book '{self.__title}' returned successfully."
        else:
            return f"Book '{self.__title}' was never taken!"
    
    def view_book_info(self):
        if self.__availability==True:
            available='Available'
            return f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {available}"
        else:
            available='Not Available'
            return f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {available}"


class Library:
    book_list=[]
    @classmethod
    def entry_book(lib,book):
        lib.book_list.append(book)
    
    @classmethod
    def display_all_books(self):
        if not self.book_list:
            print('Empty book list')
        else:
            print('Library Books:')
            for book in self.book_list:
                print(book.view_book_info())

book1 = Book(101,'Intro to DB','Chris',True)
Library.entry_book(book1)
book2 = Book(102,'Intro to Algo','Bale',True)
Library.entry_book(book2)
book3 = Book(103,'Intro to C','Benz',True)
Library.entry_book(book3)
book4 = Book(104,'Intro to CP','Case',True)
Library.entry_book(book4)
book5 = Book(105,'Intro to DP','Fede',True)
Library.entry_book(book5)
book6 = Book(106,'Mechanism of EEE ','Jude',True)
Library.entry_book(book6)
book7 = Book(107,'Dive into Data structure','Rodrygo',True)
Library.entry_book(book7)
book8 = Book(108,'Design of your code guide','Kroos',True)
Library.entry_book(book8)

def menu():
    while True:
        print('\n------------- Welcome to the Library -------------')
        print('1. View All Books')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. Exit\n')

        try:
            ch = int(input('Enter your choice: '))
            if ch==1:
                Library.display_all_books()
            elif ch==2:
                try:
                    bookID=int(input('\nEnter Book ID to borrow: '))
                    target=None
                    for book in Library.book_list:
                        if book.book_id == bookID:
                            target=book
                            break
                    if target is not None:
                        print(target.borrow_book())
                    else:
                        print('\nInvalid book ID')
                except ValueError:
                    print('\nPlease enter a valid number!!!')        
            elif ch==3:
                try:
                    bookID=int(input('\nEnter Book ID to return: '))
                    target=None
                    for book in Library.book_list:
                        if book.book_id == bookID:
                            target=book
                            break
                    if target is not None:
                        print(target.return_book())
                    else:
                        print('\nInvalid book ID')
                except ValueError:
                    print('\nPlease enter a valid number!!!')
            elif ch==4:
                print('\nExiting the Library system...')
                break
            else:
                print('\nInvalid choice! Choose an option between 1 to 4.')
        except ValueError:
            print('\nPlease enter a valid number!!!')

menu()
