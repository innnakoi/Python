a = input()
b = input()

m = len(b)
count = 0

for i in range(len(a) - m + 1):
    sub = a[i:i+m]
    ok = False
    for k in range(m):
        if b[k:] + b[:k] == sub:
            ok = True
    if ok:
        count += 1

print(count)
