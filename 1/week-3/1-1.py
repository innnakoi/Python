import math

def area_circle(r):
    return math.pi * r * r

def area_rectangle(a, b):
    return a * b

def area_triangle(a, h):
    return 0.5 * a * h

r = int(input("Enter radius of circle: "))
print("Circle area:", area_circle(r))

a, b = map(int, input("Enter rectangle sides: ").split())
print("Rectangle area:", area_rectangle(a, b))

a, h = map(int, input("Enter triangle base and height: ").split())
print("Triangle area:", area_triangle(a, h))
