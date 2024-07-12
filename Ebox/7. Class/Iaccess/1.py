class Shape:
    def area(self):
        pass

class CalAreaSquare(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Side of Square : {self.side}")
        print(f"Area of Square : {self.side * self.side}")

class CalAreaRectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.width}")
        print(f"Area of Rectangle : {self.length * self.width}")

class CalAreaTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
        print(f"Area of Triangle : {(0.5 * self.base * self.height):.2f}")

class CalAreaCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Radius of Circle : {self.radius}")
        print(f"Area of Circle : {3.14 * self.radius * self.radius:.2f}")

def main():
    print("Select an Option")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")

    option = int(input())

    if option == 1:
        side = int(input("Enter the side length of the Square\n"))
        square = CalAreaSquare(side)
        square.area()
    elif option == 2:
        length = int(input("Enter the length\n"))
        width = int(input("Enter the breadth\n"))
        rectangle = CalAreaRectangle(length, width)
        rectangle.area()
    elif option == 3:
        base = int(input("Enter the base\n"))
        height = int(input("Enter the height\n"))
        triangle = CalAreaTriangle(base, height)
        triangle.area()
    elif option == 4:
        radius = int(input("Enter the radius\n"))
        circle = CalAreaCircle(radius)
        circle.area()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()