a = input().split()


n = []
c = []

for x in a:
    if x in n:
        c[n.index(x)] += 1
    else:
        n.append(x)
        c.append(1)


print("Frequency:")
for i in range(len(n)):
    print(n[i], ":", c[i])


max_count = max(c)
for i in range(len(n)):
    if c[i] == max_count:
        print("Most popular item:", n[i])
        break


print("1 sold:", end=" ")
for i in range(len(n)):
    if c[i] == 1:
        print(n[i], end=" ")
print()


for _ in range(len(n)):
    max_count = -1
    idx = -1
    for i in range(len(c)):
        if c[i] > max_count:
            max_count = c[i]
            idx = i
    print(n[idx], c[idx])
    c[idx] = -1  

