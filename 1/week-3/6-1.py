A, B = map(int, input("Enter two numbers: ").split())

g = 1
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        g = i

l = A * B // g

print("GCD:", g)
print("LCM:", l)
