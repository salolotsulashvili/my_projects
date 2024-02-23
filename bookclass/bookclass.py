booklist={
    "name": "harry potter",
    "author": "J.K.Rowling",
    "year": "2001",
    "name2": "sofis choice",
    "author2": "william stairon",
    "year2": "2014",
    "name3": "it",
    "author3": "Jemal karchxadze",
    "year3": "2015"
}

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class BookManager:
    def __init__(self):
        self.books = []
        self.booklist = {}

    def add_book(self, title, author, year):
        if title and author and year:
            try:
                year = int(year)
                if year < 0:
                    print("Year must be a positive integer.")
                    return
            except ValueError:
                print("Year must be an integer.")
                return
       
            count = len(self.books)
            self.booklist[f"name{count}"] = title
            self.booklist[f"author{count}"] = author
            self.booklist[f"year{count}"] = str(year)
        else:
            print("Please provide valid information for title, author, and year.")


    def show_all_books(self):
        if not self.books:
            print("No books in the list.")
        else:
            print("List of all books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book found - Title: {book.title}, Author: {book.author}, Year: {book.year}")
                found = True
                break
        if not found:
            print("Book not found.")


def main():
    book_manager = BookManager()
    
    while True:
        print("\nWelcome to the Book Management System!")
        print("1. Add a new book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            booklist["name4"] = input("enter the title of the book - ")
            booklist["author4"] = input("enter the author of the book - ")
            booklist["year4"] = input("enter the year of publication - ")
            print("updated booklist is", booklist)
        elif choice == "2":
          print(booklist)        
        elif choice == "3":
            title = input("Enter the title of the book you want to search: ")
            book_manager.search_book(title)
        elif choice == "4":
            print("Thank you for using the Book Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()