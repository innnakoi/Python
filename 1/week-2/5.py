letters = "ABCEHKMOPTXY"

n = int(input())

for i in range(n):
    p = input()

    if len(p) != 6:
        print("No")
        continue

    if p[0] not in letters:
        print("No")
        continue

    if not p[1].isdigit():
        print("No")
        continue
    if not p[2].isdigit():
        print("No")
        continue
    if not p[3].isdigit():
        print("No")
        continue

    if p[4] not in letters:
        print("No")
        continue
    if p[5] not in letters:
        print("No")
        continue

    print("Yes")
