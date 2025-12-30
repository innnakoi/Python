n = int(input("Enter n: "))

for i in range(1, n + 1):
    digits = [int(d) for d in str(i)]
    if all(d != 0 and i % d == 0 for d in digits):
        print(i, end=" ")
