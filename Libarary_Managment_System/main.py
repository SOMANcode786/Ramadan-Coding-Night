# Simple Book Library System

# List to store books
library = []

# Function to add a new book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read = input("Have you read the book? (yes/no): ").lower()

    if read == "yes":
        read_status = True
    else:
        read_status = False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("Book added successfully!\n")

# Function to remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            found = True
            print("Book removed successfully!\n")
            break
    if not found:
        print("Book not found!\n")

# Function to search for a book
def search_book():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print_book(book)
            found = True
    if not found:
        print("No book found with that title or author.\n")

# Function to show all books
def display_books():
    if not library:
        print("Library is empty.\n")
    else:
        for book in library:
            print_book(book)

# Function to show statistics
def show_statistics():
    total = len(library)
    read_books = sum(1 for book in library if book["read"])
    if total > 0:
        percent_read = (read_books / total) * 100
    else:
        percent_read = 0

    print(f"Total books: {total}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percent_read:.2f}%\n")

# Helper function to print a single book
def print_book(book):
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Year:", book["year"])
    print("Genre:", book["genre"])
    print("Read:", "Yes" if book["read"] else "No")
    print("-" * 30)

# Main menu loop
def menu():
    while True:
        print("=== Book Library Menu ===")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

# Start the program
menu()
