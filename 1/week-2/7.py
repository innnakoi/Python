items = input().split()


names = []
counts = []

for x in items:
    if x in names:
        counts[names.index(x)] += 1
    else:
        names.append(x)
        counts.append(1)


print("Purchase frequency:")
for i in range(len(names)):
    print(names[i], ":", counts[i])


max_count = max(counts)
for i in range(len(names)):
    if counts[i] == max_count:
        print("Most popular item:", names[i])
        break


print("Purchased once:", end=" ")
for i in range(len(names)):
    if counts[i] == 1:
        print(names[i], end=" ")
print()


for _ in range(len(names)):
    max_count = -1
    idx = -1
    for i in range(len(counts)):
        if counts[i] > max_count:
            max_count = counts[i]
            idx = i
    print(names[idx], counts[idx])
    counts[idx] = -1  
