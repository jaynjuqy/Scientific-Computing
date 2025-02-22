import math

def calculate_area(shape: str, dimension1: float, dimension2: float = 0) -> None:
    if shape != "circle" and dimension2 == 0:
        print("The shape you have provided cannot have one dimension. Please provide the second dimension")
        return

    if shape == "circle" and dimension1:
        circle_area = math.pi * dimension1 * dimension1
        print(f'Your circle of radius {dimension1} units is {circle_area} square units')
        return
    elif shape == "rectangle" and dimension1 and dimension2:
        rect_area = dimension1 * dimension2
        print(f'The rectangle of length {dimension1} units and width of {dimension2} units is {rect_area} square units in area')
        return
    elif shape == "triangle" and dimension1 and dimension2:
        triangle_area = (dimension1 * dimension2) / 2
        print(f'Triangle of base {dimension1} units and of height {dimension2} units is {triangle_area} square units in area')
        return
    else:
        print("Shape provided is not supported or dimensions are not provided correctly")
        return

if __name__ == "__main__":
    shape = input("Input shape you wish to calculate the area of: ")

    if shape == "circle":
        radius = float(input("Input radius of the circle: "))
        calculate_area(shape, radius)
    elif shape == "rectangle":
        length = float(input("Input length of the rectangle: "))
        width = float(input("Input width of the rectangle: "))
        calculate_area(shape, length, width)
    elif shape == "triangle":
        base = float(input("Input the base of the triangle: "))
        height = float(input("Input the height of the triangle: "))
        calculate_area(shape, base, height)
    else:
        print("Error: Shape provided is not supported by the area function.")
