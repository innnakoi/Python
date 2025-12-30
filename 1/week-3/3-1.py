import math

def hy(a, b):
    return int(math.sqrt(a*a + b*b))

a1, b1 = map(float, input("Enter sides of first triangle: ").split())
a2, b2 = map(float, input("Enter sides of second triangle: ").split())

h1 = hy(a1, b1)
h2 = hy(a2, b2)

print("Hypotenuse 1:", h1,)
print("Hypotenuse 2:", h2,)

if h1 > h2:
    print("First is greater")
else:
    print("Second is greater")
