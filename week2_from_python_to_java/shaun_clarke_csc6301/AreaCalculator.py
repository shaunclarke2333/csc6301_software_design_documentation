"""Area calculator module for geometric area calculations.

Author: Shaun Clarke
Version: 2.0
Course: CSC6301
Date: 5/22/2026

Provides the AreaCalculator class with utility methods for computing
the area of basic geometric shapes. This version supports rectangle
and triangle area calculations and includes an interactive prompt
that asks the user for their name, the shape to calculate, and the
required dimensions.

Typical usage would be:
    from area_calculator import AreaCalculator

    calc: AreaCalculator = AreaCalculator()
    rect_area: float = calc.calculate_rectangle_area(length=10.0, width=2.0)
    tri_area: float = calc.calculate_triangle_area(base=10.0, height=4.0)

To run interactively:
    python area_calculator.py
"""

__author__ = "Shaun Clarke"
__version__ = "2.0"


class AreaCalculator:
    """Provides utility methods for geometric area calculations.

    An AreaCalculator instance exposes methods for computing the area
    of geometric shapes. The class itself holds no state; each method
    operates purely on the parameters provided to it. This mirrors the
    Java utility class pattern but in Python.

    Attributes:
        None. AreaCalculator is a stateless utility class.
    """

    def __init__(self) -> None:
        """Create a new AreaCalculator instance.

        The constructor takes no arguments and performs no setup, as
        the class is stateless. It exists to mirror the Java
        AreaCalculator() default constructor.
        """

        pass

    def calculate_rectangle_area(self, length: float, width: float) -> float:
        """Calculate the area of a rectangle based on its length and width.

        Multiplies the two supplied dimensions and returns the result.
        Both inputs are expected to be non negative floating point
        values representing the rectangle's sides in the same unit.

        Parameters:
            length : float
                The vertical or horizontal extent of the rectangle.
            width : float
                The horizontal or vertical extent of the rectangle.

        Returns:
            float
                The total area as the product of length and width.
        """

        area: float = length * width
        return area

    def calculate_triangle_area(self, base: float, height: float) -> float:
        """Calculate the area of a triangle based on its base and height.

        Applies the standard formula (base * height) / 2 to compute
        the area of a triangle. Both inputs are expected to be
        non-negative floating point values measured in the same unit.

        Parameters:
            base : float
                The length of the triangle's base.
            height : float
                The perpendicular height from the base to the opposite
                vertex.

        Returns:
            float
                The total area as (base * height) / 2.
        """

        area: float = (base * height) / 2
        return area


def main() -> None:
    """Run the interactive AreaCalculator prompt.

    Prompts the user for their name, asks them to choose a shape
    rectangle or triangle, collects the required dimensions, and
    prints a personalized message containing the calculated area.

    Notes:
        Input is read with the built-in input() function, which is
        Python's equivalent of Java's java.util.Scanner. An if elif
        block dispatches to the correct calculation method based on
        the user's choice.
    """

    calc: AreaCalculator = AreaCalculator()

    name: str = input("Please enter your name: ")

    print("Choose a conversion type:")
    print("Press 1 for Rectangle Area")
    print("Press 2 for Triangle Area")
    choice: str = input().strip()

    if choice == "1":
        length: float = float(input("Enter length: "))
        width: float = float(input("Enter width: "))
        area: float = calc.calculate_rectangle_area(length, width)
        print(f"Hello {name}, the calculated area is: {area}")

    elif choice == "2":
        base: float = float(input("Enter base: "))
        height: float = float(input("Enter height: "))
        area: float = calc.calculate_triangle_area(base, height)
        print(f"Hello {name}, the calculated area is: {area}")

    else:
        print(f"Hello {name}, that is not a valid choice. Please run again.")


if __name__ == "__main__":
    main()