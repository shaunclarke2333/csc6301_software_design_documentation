
"""Book module for the community library digitization system..

Author: Shaun Clarke
Course: CSC6301
Date: 5/16/2026

Provides the Book class for representing individual library books,
including circulation status and reading time estimation.
It allows you to add a book with the title, author, pages and also updates the book's stauts.
Whether its available, checked_out or reserved.

Typical usage would be:
    from library_book import Book
    my_book: Book = Book(title="A Man Called Boy", 
    author="Barend Nieuwstraten",pages=213, status"available")

    get_reading: float = my_book.calculate_reading_time()
    get_book_details: str = my_book.get_details()
    change_book_status: bool = my_book.update_status("reserved")

"""


class Book:
    """ Represents an individual book in the system along with its detials.

    A Book keeps track of  the details for a single book at a time.
    The status of the book is stored internally and can be modified,
    using update status. You can use get_details to get the details for the book.
    You can also calculate the reading time for a book using calculate_reading_time.

    Attributes:
    title: str
        The name of the book
    author: str
        The name of the author
    pages: int
        How many pages in the book
    status: str
        Is the boox available, reserved or checked_out
    """

    def __init__(self, title: str, author: str, pages: int, status: str) -> None:
        """Create a new Book with title, author, page count, and status.

        Parameters:
            title : str
                The title of the book.
            author : str
                The full name of the book's author.
            pages : int
                The total number of pages. Must be positive.
            status : str
                Current circulation status ('available', 'checked_out',
                'reserved').
        """

        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def calculate_reading_time(self) -> float:
        """Estimate total reading time for the book in minutes.
        Uses a fixed average reading speed of 1.5 minutes per page.

        Returns
            float
                Estimated reading time in minutes.
        """
        time_per_page: float = 1.5
        reading_time: float = self.pages * time_per_page
        return reading_time

    def get_details(self) -> str:
        """Print a formatted summary of the book's information to stdout.

        Displays title, author, page count, and status framed by
        separator lines. Does not return a value.

        Returns
            str
                formatted string with the book's full bibliography and status.
        """
        lines = [
            "Book Info",
            f"Title: {self.title}",
            f"Author: {self.author}",
            f"Pages: {self.pages}",
            f"Status: {self.status}"
        ]
        return "\n".join(lines)

    def update_status(self, new_status: str) -> bool:
        """Update the book's status.

        Parameters:
            new_status : str
                The new status to assign ('available', 'checked_out',
                'reserved').

        Returns:
            bool
                True if the status was updated successfully.
        """

        valid_statuses = {"available", "checked_out", "reserved"}

        if new_status not in valid_statuses:
            return False

        self.status = new_status
        return True


def main() -> None:
    """Run the interactive Book menu loop.

    Displays a menu that lets the user create a Book, calculate its
    estimated reading time, view its details, update its status,
    or exit the program. The loop continues until the user
    selects the exit option.

    Notes:
    A book must be created via option 1 before options 2, 3, or 4 can
    be used, since those options operate on the most recently created
    Book instance.
    """

    while True:
        # Display menu
        print("\n--- Book Menu ---")
        print("1. Add a book")
        print("2. Get the book's reading time")
        print("3. Get the book's details")
        print("4. Update the books stauts")
        print("5. Exit")

        # Get the user's selection
        choice: str = input("\nChoose an option to continue: ").strip()

        # Validating the selection
        if choice == "1":
            # Getting inputs:
            title: str = input("Enter the book's title: ")
            author: str = input("Enter the author's name: ")
            pages: int = int(input("Enter the number of pages: "))
            status: str = input("Enter the book's status: ")

            # Instantiating the book class
            new_book: Book = Book(
                title, author, pages, status
            )

        elif choice == "2":
            get_reading_time: float = new_book.calculate_reading_time()
            print(f"\nIt will take {get_reading_time} minutes to finish {title}")

        elif choice == "3":
            get_book_details: str = new_book.get_details()
            print(get_book_details)

        elif choice == "4":
            status: str = input("\nEnter the book's updated status: ")
            change_book_status: bool = new_book.update_status(status)

            if change_book_status:
                print(f"The book {title}'s status has been updated")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
