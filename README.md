# CSC6301 Software Design and Documentation

Coursework for CSC6301 Software Design and Documentation. The focus of the course, and of this repository, is writing and documenting code so that someone other than the author can read it, run it, and maintain it. Each weekly project lives in its own folder and ships with its own README that explains what it does, how to run it, and how it is designed.

## Projects

Each project runs from inside its own folder. Move into the folder first, then run the command shown.

| Week | Project | Focus | Run |
| --- | --- | --- | --- |
| [Week 1](week1_auto_code_documentation/shaun_clarke_csc6301) | Library Book Module | Automatic code documentation with pydoc | `python3 library_book.py` |
| [Week 2](week2_from_python_to_java/shaun_clarke_csc6301) | Area Calculator Module | Mapping Python design onto Java | `python3 AreaCalculator.py` |
| [Week 3](week3_defining_classes_using_java/shaun_clarke_csc6301) | Smart Home Device Manager | Defining classes: interface, inheritance, polymorphism | `python3 smart_device.py` |
| [Week 4](week4_using_java_docs_to_software_reuse/shaun_clarke_csc6301) | Flexible Notification System | Software reuse through composition | `python3 notification_app.py` |
| [Week 5](week5_sdlc/shaun_clarke_csc6301) | Notification System (Maintenance) | SDLC maintenance phase: extending without rewriting | `python3 notification_app.py` |

Click any week to open its folder and read the full project README.

## Repository structure

```
csc6301_software_design_documentation/
├── week1_auto_code_documentation/
│   └── shaun_clarke_csc6301/      Library Book Module
├── week2_from_python_to_java/
│   └── shaun_clarke_csc6301/      Area Calculator Module (two versions)
├── week3_defining_classes_using_java/
│   └── shaun_clarke_csc6301/      Smart Home Device Manager
├── week4_using_java_docs_to_software_reuse/
│   └── shaun_clarke_csc6301/      Flexible Notification System
└── week5_sdlc/
    └── shaun_clarke_csc6301/      Notification System maintenance release
```

Each `shaun_clarke_csc6301` folder holds the source for that week along with its generated documentation (pydoc HTML, UML diagrams, or PDFs) and its own README.

## Getting started

Clone the repository:

```bash
git clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation
```

Move into the project folder you want and run it. For example, Week 3:

```bash
cd week3_defining_classes_using_java/shaun_clarke_csc6301
python3 smart_device.py
```

Run every project from inside its own folder. The Week 4 and Week 5 projects are split across several modules that import each other by name, so they need to be run from their own directory.

## Requirements

* Python 3.9 or newer. Several projects use built in generic type hints such as `list[str]`, which require 3.9 or later.
* No third party packages. Every project runs on the Python standard library alone.

## Conventions

* Each project lives in its own folder with its own README, so it can be read and run on its own.
* Source files carry module level docstrings and method docstrings, and most weeks include a generated reference such as a pydoc HTML page or a UML diagram.
* Where the course maps Python onto Java, the docstrings note the Java equivalent of the design.
* Detailed run steps, menu walkthroughs, and design notes live in each project README rather than here, so there is a single source of truth for each project.

## Author

Shaun Clarke
CSC6301 Software Design and Documentation