import math


def calculate_circle_area(radius):
    """
    Calculates the area of circle.
    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    return math.pi * float(radius) ** 2


if __name__ == "__main__":
    print("Hello! I will calculate the area of a circle for you.")
    try:
        user_input = input("Please, enter the radius of the circle: ")
        radius = float(user_input)
        area = calculate_circle_area(radius)
        print(f"The area of the circle is {area:.2f}")
    except ValueError:
        print("Entered radius is not a number. Please try again.")
