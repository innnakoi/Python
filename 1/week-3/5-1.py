A, B = map(int, input("Enter A B: ").split())
C, D = map(int, input("Enter C D: ").split())

num = A*D - C*B
den = B*D
print("Result:", num, "/", den)
