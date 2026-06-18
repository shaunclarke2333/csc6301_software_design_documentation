"""Area calculator module for geometric area calculations.

Author: Shaun Clarke
Course: CSC6301
Date: 5/22/2026

Provides the AreaCalculator class with utility methods for computing
the area of basic geometric shapes. This initial version supports
rectangle area calculations based on a given length and width.

Typical usage would be:
    from area_calculator import AreaCalculator

    calc: AreaCalculator = AreaCalculator()
    area: float = calc.calculate_rectangle_area(length=5.0, width=3.0)
    print(area)
"""


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


def main() -> None:
    """Run the interactive AreaCalculator menu loop.

    Displays a menu that lets the user calculate a rectangle's area
    by entering a length and a width, or exit the program. The loop
    continues until the user selects the exit option.
    """

    calc: AreaCalculator = AreaCalculator()

    while True:
        # Display menu
        print("\n--- Area Calculator Menu ---")
        print("1. Calculate rectangle area")
        print("2. Exit")

        # Get the user's selection
        choice: str = input("\nChoose an option to continue: ").strip()

        # Validating the selection
        if choice == "1":
            length: float = float(input("Enter the rectangle's length: "))
            width: float = float(input("Enter the rectangle's width: "))

            area: float = calc.calculate_rectangle_area(length, width)
            print(f"\nThe area of the rectangle is {area}")

        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()