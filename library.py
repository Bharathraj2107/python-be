#using inheritances
#show available books
# add books from the child class and it should reflect in parent class also
Book_list = ["Python", "Java", "C"]
class Library:
    def books_Available(self):

        print("The Library has following books")
        for i in Book_list:
            print(i)
class Librarian(Library):
    def add_book(self):
        super().books_Available()#here we get the book_list not defined error
        book_name=input("enter the book name to add ")
        if book_name not in Book_list:
            Book_list.append(book_name)
        else:
            print("Book Already exists")
        super().books_Available()
l1=Librarian()
# l1.books_Available()
l1.add_book()
# l1.books_Available()#why it is not updating why we should call again