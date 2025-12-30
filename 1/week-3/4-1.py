def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input("Enter A B: ").split())
C, D = map(int, input("Enter C D: ").split())

num = A * D
den = B * C
g = gcd(num, den)

print("Result:", num//g, "/", den//g)
