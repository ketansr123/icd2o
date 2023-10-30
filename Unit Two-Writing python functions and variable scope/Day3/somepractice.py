#1
import math
def calculate_circle_area(radius):
    return math.pi*radius**2
r=4
print(f"The area of the circle with radius {r} is {calculate_circle_area(4):.2f}")
#2
def calculate_rectangle_area(length, width):
    return length*width

l=5
w=5
print(f"The area of your rectangle with length {l} and width {w} is {calculate_rectangle_area(l, w)}")



def volume_of_cylinder(radius, height):
    return math.pi*radius**2*height
r=5
h=10
print(f"The area of a cylinder with a radius {r} and height {h} is {volume_of_cylinder(r, h):.2f}")
