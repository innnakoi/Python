
def a_s(arr):
    s = sum(arr)
    avg = s / len(arr)
    return s, avg

arrays = []

for i in range(3):
    arr = list(map(int, input(f"Enter elements of array {i+1}: ").split()))
    arrays.append(arr)

for a in arrays:
    print(a_s(a))
