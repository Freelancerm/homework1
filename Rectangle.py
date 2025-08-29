from typing import Tuple


class Rectangle:
    """
    Represents a rectangle with its width and height.
    """

    def __init__(self, width: float, height: float):
        """
        Constructor for the Rectangle class.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Checks if the rectangle is a square.

        Returns:
            True if the rectangle is square, otherwise False.
        """
        return self.width == self.height

    def resize(self, new_width: float, new_height: float) -> Tuple[float, float]:
        """
        Changes the width and height of the rectangle.

        Args:
            new_width: The new width of the rectangle.
            new_height: The new height of the rectangle.

        Returns:
            A tuple containing the new width and height.
        """
        self.width = new_width
        self.height = new_height
        return self.width, self.height


if __name__ == "__main__":
    try:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))

        my_rectangle = Rectangle(width, height)

        print(f"\nRectangle Properties:")
        print(f"Area: {my_rectangle.area()}")
        print(f"Perimeter: {my_rectangle.perimeter()}")
        print(f"Is it a square? {my_rectangle.is_square()}")

        new_width_input = float(input("\nEnter a new width to resize: "))
        new_height_input = float(input("Enter a new height to resize: "))

        my_rectangle.resize(new_width_input, new_height_input)

        print(f"\nAfter Resizing:")
        print(f"New Width: {my_rectangle.width}")
        print(f"New Height: {my_rectangle.height}")
        print(f"New Area: {my_rectangle.area()}")
        print(f"New Perimeter: {my_rectangle.perimeter()}")

    except ValueError:
        print("Invalid input. Please enter a valid number for width and height.")
