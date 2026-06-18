# Library Book Module

A Book class for a community library digitization system, built for Week 1 of CSC6301 (Automatic Code Documentation). It models a single library book, estimates reading time, formats a details summary, and validates status changes. An interactive terminal menu lets you drive the class through every method.

## Class design

The module defines a single class:

* `Book` represents one library book. It stores a title, author, page count, and circulation status, where status is one of `available`, `checked_out`, or `reserved`. The class exposes three methods:
  * `calculate_reading_time()` returns the estimated reading time in minutes, using a fixed rate of 1.5 minutes per page.
  * `get_details()` returns a formatted string with the book's title, author, pages, and status.
  * `update_status(new_status)` validates the new value and updates the status. It returns `True` on success and `False` if the value is not one of the three valid statuses.

## Project structure

```
week1_auto_code_documentation/
└── shaun_clarke_csc6301/
    ├── library_book.py     Source (Book class and interactive menu)
    └── library_book.html   pydoc reference generated from the source
```

## Requirements

* Python 3.9 or newer
* No third party packages

## Getting started

Clone the repository and move into the project folder:

```bash
git clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation/week1_auto_code_documentation/shaun_clarke_csc6301
```

Run the program:

```bash
python3 library_book.py
```

## Using the menu

On start you get this menu:

```
--- Book Menu ---
1. Add a book
2. Get the book's reading time
3. Get the book's details
4. Update the book's status
5. Exit
```

Create a book first with option 1. Options 2, 3, and 4 all act on the most recently created book, so they will fail if you run them before a book exists.

* Option 1 prompts for title, author, pages, and status, then creates the book.
* Option 2 prints the estimated reading time at 1.5 minutes per page.
* Option 3 prints the formatted book details.
* Option 4 prompts for a new status and updates it. Valid values are `available`, `checked_out`, and `reserved`. Anything else is rejected.
* Option 5 exits.

### Example session

```
Choose an option to continue: 1
Enter the book's title: The Hobbit
Enter the author's name: Tolkien
Enter the number of pages: 300
Enter the book's status: available

Choose an option to continue: 2
It will take 450.0 minutes to finish The Hobbit

Choose an option to continue: 3
Book Info
Title: The Hobbit
Author: Tolkien
Pages: 300
Status: available

Choose an option to continue: 5
Goodbye!
```

## Generated documentation

The HTML reference in `library_book.html` was generated with pydoc. Open it in any browser to read the full class and method documentation.

To regenerate it after a code change, run this from inside the project folder:

```bash
python3 -m pydoc -w library_book
```

## Author

Shaun Clarke
CSC6301 Software Design and Documentation