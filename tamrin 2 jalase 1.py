import json


# ------------------------------------------
# Book Class
# ------------------------------------------
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        """Set self.title, self.author, self.year, and self.available."""
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self) -> bool:
        """Mark the book as borrowed, if it's available."""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self) -> None:
        """Mark the book as available again."""
        self.available = True

    def display(self) -> None:
        """Print the book's info on one line."""
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} ({self.year}) - {status}")


# ------------------------------------------
# User Class
# ------------------------------------------
class User:
    def __init__(self, name: str) -> None:
        """Set self.name and self.borrowed_books (start empty)."""
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> bool:
        """Try to borrow `book`; track it if successful."""
        if book.borrow():  # اگر کتاب در دسترس بود
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book: Book) -> None:
        """Return a book this user previously borrowed."""
        # فرض می‌کنیم کتاب حتماً در لیست وجود دارد
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

    def display(self) -> None:
        """Print the user's name and how many books they currently have out."""
        count = len(self.borrowed_books)
        print(f"{self.name} ({count} books borrowed)")


# ------------------------------------------
# Library Class
# ------------------------------------------
class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.users: list[User] = []

    # ---------- Book Management ----------

    def add_book(self, book: Book) -> None:
        """Add a Book object to self.books."""
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        """Remove the book with this title from self.books, if present."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break  # فقط اولین کتاب با این عنوان حذف شود

    def search_book(self, title: str) -> Book | None:
        """Find the book with this title."""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def show_all_books(self) -> None:
        """Print every book in the library (call book.display() on each)."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display()

    def show_available_books(self) -> None:
        """Print only the books where available is True."""
        available_books = [book for book in self.books if book.available]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                book.display()

    # ---------- User Management ----------

    def add_user(self, user: User) -> None:
        """Add a User object to self.users."""
        self.users.append(user)

    def search_user(self, name: str) -> User | None:
        """Find the user with this name."""
        for user in self.users:
            if user.name == name:
                return user
        return None

    # ---------- Borrow / Return ----------

    def borrow_book(self, user_name: str, book_title: str) -> None:
        """Look up the user and book by name/title, then borrow."""
        user = self.search_user(user_name)
        book = self.search_book(book_title)

        if user is None:
            print("User not found.")
            return
        if book is None:
            print("Book not found.")
            return

        # تلاش برای امانت گرفتن کتاب توسط کاربر
        if user.borrow_book(book):
            print(f"'{book_title}' borrowed successfully by {user_name}.")
        else:
            print(f"'{book_title}' is already borrowed.")

    def return_book(self, user_name: str, book_title: str) -> None:
        """Look up the user and book by name/title, then return."""
        user = self.search_user(user_name)
        book = self.search_book(book_title)

        if user is None:
            print("User not found.")
            return
        if book is None:
            print("Book not found.")
            return

        # بررسی اینکه آیا کاربر این کتاب را به امانت دارد
        if book in user.borrowed_books:
            user.return_book(book)
            print(f"'{book_title}' returned successfully by {user_name}.")
        else:
            print(f"{user_name} does not have '{book_title}' borrowed.")

    # ---------- File Handling ----------

    def save_books(self, filename: str) -> None:
        """Save self.books to a file, one book per record."""
        data = []
        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "available": book.available
            })
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Books saved to '{filename}'.")

    def load_books(self, filename: str) -> None:
        """Load books from a file previously written by save_books."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return
        except json.JSONDecodeError:
            print(f"File '{filename}' is not a valid JSON.")
            return

        # پاک کردن لیست فعلی و جایگزینی با کتاب‌های جدید
        self.books = []
        for item in data:
            book = Book(item["title"], item["author"], item["year"])
            book.available = item["available"]  # تنظیم وضعیت موجود بودن از فایل
            self.books.append(book)
        print(f"Books loaded from '{filename}'. ({len(self.books)} books)")


# ------------------------------------------
# User Interface
# ------------------------------------------
def print_menu():
    print("\n========== Library Management ==========")
    print("Available commands:")
    print("  add_book")
    print("  remove_book")
    print("  search_book")
    print("  show_all_books")
    print("  show_available_books")
    print("  add_user")
    print("  search_user")
    print("  borrow_book")
    print("  return_book")
    print("  save_books")
    print("  load_books")
    print("  exit")


def run(library):
    while True:
        print_menu()

        command = input("\nCommand: ").strip().lower()

        match command:

            case "add_book":
                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))

                book = Book(title, author, year)
                library.add_book(book)

            case "remove_book":
                title = input("Title: ")
                library.remove_book(title)

            case "search_book":
                title = input("Title: ")
                result = library.search_book(title)

                if result:
                    result.display()
                else:
                    print("Book not found.")

            case "show_all_books":
                library.show_all_books()

            case "show_available_books":
                library.show_available_books()

            case "add_user":
                name = input("User name: ")

                user = User(name)
                library.add_user(user)

            case "search_user":
                name = input("User name: ")
                result = library.search_user(name)

                if result:
                    result.display()
                else:
                    print("User not found.")

            case "borrow_book":
                user_name = input("User name: ")
                book_title = input("Book title: ")

                library.borrow_book(user_name, book_title)

            case "return_book":
                user_name = input("User name: ")
                book_title = input("Book title: ")

                library.return_book(user_name, book_title)

            case "save_books":
                filename = input("File name: ")
                library.save_books(filename)

            case "load_books":
                filename = input("File name: ")
                library.load_books(filename)

            case "exit":
                print("Goodbye!")
                break

            case _:
                print("Unknown command.")


# ------------------------------------------
# Main
# ------------------------------------------
if __name__ == "__main__":

    # Create a library
    library = Library()

    # Create some books
    clean_code = Book("Clean Code", "Robert C. Martin", 2008)
    python_crash_course = Book("Python Crash Course", "Eric Matthes", 2023)

    # Create a user
    alice = User("Alice")

    # Add data to the library
    library.add_book(clean_code)
    library.add_book(python_crash_course)
    library.add_user(alice)

    # Example method calls
    library.show_all_books()
    library.search_book("Clean Code")

    # Start the application
    run(library)