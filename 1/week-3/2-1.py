import math

def t_a(a, h):
    return 0.5 * a * h

def h_a(a):
    h = a * math.sqrt(3) / 2
    return 6 * t_a(a, h)

a = int(input("Enter side of hexagon: "))
h = int(input("Enter height of hexagon: "))
print("Hexagon area:", h_a(a))
