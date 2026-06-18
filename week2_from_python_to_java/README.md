Area Calculator Module

An AreaCalculator class that computes the area of basic geometric shapes, built for Week 2 of CSC6301 (From Python to Java). The class is a stateless utility class, modeled on the Java utility class pattern, where every method works only on the parameters passed to it. This folder holds two versions of the program plus generated documentation for each.

Which file is which

This folder contains two versions. Read this first so you run the right one.

FileVersionShapesHow it runsAreaCalculator1.pyVersion 1 (first build)Rectangle onlyMenu loop that repeats until you exitAreaCalculator.pyVersion 2.0 (latest)Rectangle and triangleSingle pass that greets you by name

The file with the 1 suffix is the earlier version. The unsuffixed AreaCalculator.py is the newer version 2.0 and is the one to run if you just want the full program.

What it does

Version 2.0 (AreaCalculator.py)

Provides two calculations through one class:


calculate_rectangle_area(length, width) returns length times width.
calculate_triangle_area(base, height) returns (base times height) divided by 2.


When run directly, it asks for your name, asks whether you want a rectangle or a triangle, collects the dimensions, and prints a personalized result. It runs once and exits.

Version 1 (AreaCalculator1.py)

Provides rectangle area only through calculate_rectangle_area(length, width). When run directly, it shows a menu that loops, so you can calculate several rectangles in a row before choosing exit.

Project structure

week2_from_python_to_java/

└── shaun_clarke_csc6301/
    
    ├── AreaCalculator.py                      Version 2.0 source (rectangle and triangle)
    
    ├── AreaCalculator1.py                     Version 1 source (rectangle only)
    
    ├── AreaCalculator.html                    pydoc reference for version 2.0
    
    ├── AreaCalculator1.html                   pydoc reference for version 1
    
    ├── Python_ module AreaCalculator.pdf      PDF export of the version 2.0 reference
    
    ├── Python_ module AreaCalculator1.pdf     PDF export of the version 1 reference
    
    └── AreaCalculator.zip                     Bundle of the version 2.0 source and its PDF

Requirements


Python 3.9 or newer
No third party packages


Getting started

Clone the repository and move into the project folder:

bashgit clone https://github.com/shaunclarke2333/csc6301_software_design_documentation.git
cd csc6301_software_design_documentation/week2_from_python_to_java/shaun_clarke_csc6301

Run version 2.0:

bashpython3 AreaCalculator.py

Run version 1:

bashpython3 AreaCalculator1.py

Using the program

Version 2.0 example

Please enter your name: Shaun
Choose a conversion type:
Press 1 for Rectangle Area
Press 2 for Triangle Area
2
Enter base: 10
Enter height: 4
Hello Shaun, the calculated area is: 20.0

Press 1 for a rectangle and enter length then width. Press 2 for a triangle and enter base then height. Any other choice prints a message and the program ends, so run it again to retry.

Version 1 example

--- Area Calculator Menu ---
1. Calculate rectangle area
2. Exit

Choose an option to continue: 1
Enter the rectangle's length: 5
Enter the rectangle's width: 3

The area of the rectangle is 15.0

Choose 1 to calculate a rectangle area, then enter length and width. The menu repeats so you can keep going. Choose 2 to exit.

Generated documentation

The HTML references were generated with pydoc. Open either file in any browser to read the full class and method documentation.


AreaCalculator.html documents version 2.0.
AreaCalculator1.html documents version 1.


To regenerate a reference after a code change, run this from inside the project folder. Use the module name without the .py extension:

bashpython3 -m pydoc -w AreaCalculator

Author

Shaun Clarke
CSC6301 Software Design and Documentation