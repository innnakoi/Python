import math

a, b, c, d, diag = map(float, input("Enter 4 sides and diagonal: ").split())

def triangle_area(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x:
        return 0   
    s = (x + y + z) / 2
    return math.sqrt(s * (s - x) * (s - y) * (s - z))

area1 = triangle_area(a, b, diag)
area2 = triangle_area(c, d, diag)

if area1 == 0 or area2 == 0:
    print("diagonal and sides do not form triangles")
else:
    print("Area:", area1 + area2)
