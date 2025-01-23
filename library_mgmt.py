library = []
demo_books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "9780743273565", "copies": 5, "borrow": 0, "available": 5},
    {"title": "1984", "author": "George Orwell", "isbn": "9780451524935", "copies": 8, "borrow": 0, "available": 8},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "9780061120084", "copies": 7, "borrow": 0, "available": 7},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "9780316769488", "copies": 6, "borrow": 0, "available": 6},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "9781503290563", "copies": 10, "borrow": 0, "available": 10},
]
library.extend(demo_books)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    copies = int(input("Enter total copies: "))
    borrow = 0
    available = copies-borrow
    book = {"title": title,"author": author,"isbn" : isbn,"copies":copies,"borrow": borrow, "available": available,}
    library.append(book)
    
def view_invent():
    print("--- Library Inventory ---")
    for i in library:
        print(f"Title: {i['title']}, Author: {i['author']}, ISBN: {i['isbn']}, Total: {i['copies']}, Borrowed: {i['borrow']} , Available: {i['available']}")
        
def delete_book():
    isbn_temp = input("Enter ISBN: ")
    print("Current Library")
    view_invent()
    print("Finding Book")
    found = False
    for i, book in enumerate(library):
        if book['isbn']==isbn_temp:
            print("Book Found")
            found = True
            library.pop(i)
            print("Book Deleted")
    if not found:
        print("Book does not exist")
    print("Updated Library")
    view_invent()

def return_book():
    print("====Return Books====")
    isbn_temp = input("Enter ISBN: ")
    book_returned = int(input("Enter No. of books to return: "))
    for i, book in enumerate(library):
        if book["isbn"]==isbn_temp:
            print("book found") 
            book['available'] += book_returned
            book['borrow'] -= book_returned
            print("book Returned")
            print(library[i])
    

def borrow_book():
    print("====Borrow Books====")
    isbn_temp = input("Enter ISBN: ")
    book_borrow = int(input("Enter No. of books to borrow: "))
    for i, book in enumerate(library):
        if book["isbn"]==isbn_temp:
            print("book found") 
            book['available'] -= book_borrow
            book['borrow'] += book_borrow
            print("book Borrowed")
            print(library[i])
    
def main_menu():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Inventory")
        print("5. Delete Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice =="1":
            add_book()
        elif choice =="2":
            borrow_book()
        elif choice =="3":
            return_book()
        elif choice =="4":
            view_invent()
        elif choice =="5":
            delete_book()
        elif choice =="6":
            print("Good Bye")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
