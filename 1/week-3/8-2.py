m = int(input("Enter length: "))
arr = list(map(int, input("Enter array: ").split()))

print("Original:", arr)
arr[0], arr[-1] = arr[-1], arr[0]
print("Result:", arr)
