# Is project mein hum ye concepts use karenge:

# Feature	Concept
# 1. Book Name	    variables
# 2. Add Book   	list
# 3. Show Books	    function
# 4. Search Book	if-else
# 5. Borrow Book	list/operators
# 6. Return Book	list
# 7. Exit      	    while loop


# ------------------------------------------
# Library Data
# ------------------------------------------

books = []


# ------------------------------------------
# Add Book Function
# ------------------------------------------
def add_book():
    book_name = input("Enter book name: ")

    books.append(book_name)

    print("Book added successfully!")
# ------------------------------------------
# Show Books Function
# ------------------------------------------

def show_books():
    print("\n----- LIBRARY BOOKS -----")

    if len(books) == 0:
        print("No books available in the library.")
    else:
        for book in books:
            print(book)
# ------------------------------------------
# Search Book Function
# ------------------------------------------

def search_book():
    book_name = input("Enter book name to search: ")

    if book_name in books:
        print("Book is available.")

    else:
        print("Book is not available.")


# ------------------------------------------
# Borrow Book Function
# ------------------------------------------

def borrow_book():

    book_name = input("Enter book name to borrow: ")

    if book_name in books:

        books.remove(book_name)

        print("Book borrowed successfully!")

    else:

        print("Book is not available.")


# ------------------------------------------
# Return Book Function
# ------------------------------------------

def return_book():

    book_name = input("Enter book name to return: ")

    books.append(book_name)

    print("Book returned successfully!")


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n----- LIBRARY MANAGEMENT SYSTEM -----")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        show_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        borrow_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")