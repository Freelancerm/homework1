

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + self.height
    def is_square(self):
        return self.width == self.height
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        return new_width, new_height


try:
    params = rectangle(float(input("Width: ")), float(input("Height: ")))
    print(f"Area of your rectangle is {params.area()}")
    print(f"Perimetr of your rectangle is {params.perimeter()}")
    print(f"Is it Square?(False or True) = {params.is_square()}")
    resize = rectangle.resize(params, float(input("Enter new width:")), float(input("Enter new height:")))
    print(f"Resize of your rectangle is {resize}")
except:
    print("Entered width or height is not a number. Try again")

