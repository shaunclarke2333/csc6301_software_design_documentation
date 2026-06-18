# Area Calculator Module

An `AreaCalculator` class that computes the area of basic geometric shapes, built for Week 2 of CSC6301 (From Python to Java). The class is a stateless utility class, modeled on the Java utility class pattern, where every method works only on the parameters passed to it. This folder holds two versions of the program plus generated documentation for each. An interactive prompt lets you drive the class from the terminal.

## Which file is which

This folder contains two versions. Read this first so you run the right one.

| File | Version | Shapes | How it runs |
| --- | --- | --- | --- |
| `AreaCalculator1.py` | Version 1 (first build) | Rectangle only | Menu loop that repeats until you exit |
| `AreaCalculator.py` | Version 2.0 (latest) | Rectangle and triangle | Single pass that greets you by name |

The file with the `1` suffix is the earlier version. The unsuffixed `AreaCalculator.py` is the newer version 2.0 and is the one to run if you just want the full program.

## Class design

Both versions define a single class, `AreaCalculator`. It is a stateless utility class, so it holds no state and every method works only on the parameters passed to it. This mirrors the Java utility class pattern.

* Version 1 (`AreaCalculator1.py`) exposes one method:
  * `calculate_rectangle_area(length, width)` returns length times width.
* Version 2.0 (`AreaCalculator.py`) keeps that method and adds a second:
  * `calculate_triangle_area(base, height)` returns (base times height) divided by 2.

## Project structure

```
week2_from_python_to_java/
└── shaun_clarke_csc6301/
    ├── AreaCalculator.py                      Version 2.0 source (rectangle and triangle)
    ├── AreaCalculator1.py                     Version 1 source (rectangle only)
    ├── AreaCalculator.html                    pydoc reference for version 2.0
    ├── AreaCalculator1.html                   pydoc reference for version 1
    ├── Python_ module AreaCalculator.pdf      PDF export of the version 2.0 reference
    ├── Python_ module AreaCalculator1.pdf     PDF export of the version 1 reference
    └── AreaCalculator.zip                     Bundle of the version 2.0 source and its PDF
```

## Requirements

* Python 3.9 or newer
* No third party packages

## Getting started

Clone the repository and move into the project folder:

```bash
git clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation/week2_from_python_to_java/shaun_clarke_csc6301
```

Run version 2.0:

```bash
python3 AreaCalculator.py
```

Run version 1:

```bash
python3 AreaCalculator1.py
```

## Using the program

### Version 2.0 (`AreaCalculator.py`)

It asks for your name, asks whether you want a rectangle or a triangle, collects the dimensions, and prints a personalized result. It runs once and exits, so run it again to do another calculation.

* Press 1 for a rectangle, then enter length and width.
* Press 2 for a triangle, then enter base and height.
* Any other choice prints a message and the program ends.

```
Please enter your name: Shaun
Choose a conversion type:
Press 1 for Rectangle Area
Press 2 for Triangle Area
2
Enter base: 10
Enter height: 4
Hello Shaun, the calculated area is: 20.0
```

### Version 1 (`AreaCalculator1.py`)

It shows a menu that loops, so you can calculate several rectangles in a row before choosing exit.

* Option 1 calculates a rectangle area. Enter length and width.
* Option 2 exits.

```
--- Area Calculator Menu ---
1. Calculate rectangle area
2. Exit

Choose an option to continue: 1
Enter the rectangle's length: 5
Enter the rectangle's width: 3

The area of the rectangle is 15.0
```

## Generated documentation

The HTML references were generated with pydoc. Open either file in any browser to read the full class and method documentation.

* `AreaCalculator.html` documents version 2.0.
* `AreaCalculator1.html` documents version 1.

To regenerate a reference after a code change, run this from inside the project folder. Use the module name without the .py extension:

```bash
python3 -m pydoc -w AreaCalculator
```

## Author

Shaun Clarke
CSC6301 Software Design and Documentation