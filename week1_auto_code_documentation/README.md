# csc6301_software_design_documentation

Tracking my Software Design & Documentation class assignments.

## About

This repository collects my coursework for CSC 6301 Software Design & Documentation. The focus of the course, and of this repo, is learning the right way to write and document code, so each project is organized to be read, run, and maintained by someone other than the author.

## Getting started

Clone the repository and move into it:

```bash
git clone <repo-url>
cd csc6301_software_design_documentation
```

Each project lives in its own folder and ships with its own run instructions in the sections below. Run every project from inside its own folder unless a section says otherwise.

## Projects

| Project | Week | Summary | Run |
| --- | --- | --- | --- |
| Library Book Module | 1 | Book class for a community library system, with reading time, status updates, and an interactive menu | `python3 library_book.py` |

## Project details

### Library Book Module

Folder: `week1_auto_code_documentation/shaun_clarke_csc6301`

Week 1, automatic code documentation.

A Book class for a community library digitization system. Each book holds a title, author, page count, and circulation status of available, checked_out, or reserved. The class estimates reading time, returns a formatted details summary, and updates the status with validation. An interactive menu lets you exercise all of it from the terminal.

Prerequisites:

* Python 3.9 or newer
* No third party packages

Run it:

```bash
cd week1_auto_code_documentation/shaun_clarke_csc6301
python3 library_book.py
```

Using the menu. Create a book first with option 1, then the other options act on that book.

```
--- Book Menu ---
1. Add a book
2. Get the book's reading time
3. Get the book's details
4. Update the book's status
5. Exit
```

* Option 1 prompts for title, author, pages, and status, then creates the book.
* Option 2 prints the estimated reading time at 1.5 minutes per page.
* Option 3 prints the formatted book details.
* Option 4 updates the status. Valid values are available, checked_out, and reserved.
* Option 5 exits.

Documentation. The HTML reference was generated with pydoc. Open `library_book.html` in any browser to read it. To regenerate it after a code change:

```bash
python3 -m pydoc -w library_book
```