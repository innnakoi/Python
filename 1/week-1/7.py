a = int(input("First number: "))
b = int(input("Second number: "))
c= input("Operation: ")

if c=="+":
    print(a + b)
elif c=="-":
    print(a - b)
elif c=="*":
    print(a * b)
elif c=="/":
    print(a / b)

if c == "/" and b == 0:
    print("Error")