booklist = []
shelflist = []
class Library(object):
    def __init__(self, library_name):
        self.name = library_name

    def print_all_books(self):
        for item in booklist:
            print item.title + " by " + item.author 
#Prints the title and author of all the books in the library

    def number_of_books(self):
        print len(booklist)
    

    def number_of_shelves(self):
        print len(shelflist)
        
#Prints the number of shelves in the library
        
class Shelf(Library):
    def __init__(self, shelf_number):
        self.shelf_number = shelf_number
        shelflist.append(self)
        
#Stipulates that each shelf has a shelf number and adds the shelf to a list of all library shelves

    def booksonthisshelf(self):
        for item in booklist:
            if item.shelf_number == self.shelf_number:
                print item.title + " by " + item.author
#Prints the books on a given shelf

class Book(Library):
    def __init__(self, title, author, shelf_number):
        self.title = title
        self.author = author
        self.shelf_number = shelf_number
        booklist.append(self)

    def print_book(self):
        print self.title + " by " + self.author
#Prints a single book
    
    def reshelf(self, newshelf):
        self.shelf_number = newshelf
        print self.title + " by " + self.author + " has been moved to shelf " + str(newshelf)
#Moves a book to a new shelf

    def unshelf(self):
        self.shelf_number = "Book not on shelf"
#Removes a book from a shelf

    def whichshelf(self):
        print self.shelf_number
#Prints the shelf number of a single book
    
    def erasebook(self):
        for item in booklist:
            if item == self:
                itemindex = booklist.index(self)
                del booklist[itemindex]
        print self.title + " by " + self.author + " has been removed from the library."
#Erases a book from the library and it's respective shelf


my_library = Library("Lily's Library")        
shelf1 = Shelf(1)
shelf2 = Shelf(2)
tkam = Book("To Kill a Mockingbird", "H Lee", 1)
lolita = Book("Lolita", "V Nabokov", 2)
ledwo = Book("Let's Explore Diabetes with Owls", "D Sedaris", 2)
wm = Book("Watchmen", "A Moore", 1)

my_library.print_all_books()
print lolita.shelf_number
lolita.reshelf(1)
print lolita.shelf_number
shelf1.booksonthisshelf()
lolita.erasebook()
my_library.print_all_books()
my_library.number_of_shelves()

#!/usr/bin/env python

