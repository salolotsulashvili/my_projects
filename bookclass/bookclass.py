import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        try:
            int(author)  
            raise ValueError("Author must be a string.")
        except ValueError:
            self.author = author
        try:
            self.publication_year = int(publication_year)
            current_year = datetime.datetime.now().year
            if self.publication_year > current_year:
                raise ValueError("Publication year cannot be in the future.")
        except ValueError as e:
            raise e

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = input("Enter the publication year of the book: ")
            try:
                book = Book(title, author, publication_year)
                library.add_book(book)
                print("Book added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter the title of the book you want to search: ")
            found_book = library.search_book(title)
            if found_book:
                print(f"Book found - Title: {found_book.title}, Author: {found_book.author}, Publication Year: {found_book.publication_year}")
            else:
                print("Book not found in the library.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
