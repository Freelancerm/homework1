import math


def calculate_circle_area(radius):
    try:
        radius = math.pi * float(radius) ** 2
        print(f"The area of circle is {radius}")
    except:
        print("Entered radius is not a number. Try again")



print("Hello! I will calculate area of circle for you")
calculate_circle_area(input("Please, enter radius of circle:"))
