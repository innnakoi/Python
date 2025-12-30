def in_cir(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 < r*r

a, b, r = map(float, input("Enter center and radius: ").split())
n = int(input("Enter number of points: "))

count = 0
for i in range(n):
    x, y = map(float, input("Enter point: ").split())
    if in_cir(x, y, a, b, r):
        count += 1

print("Points inside:", count)