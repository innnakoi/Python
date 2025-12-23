w = input("enter a words ").split()

max_len = 0
for s in w:
    if len(s) > max_len:
         max_len = len(s)

    res = []
for s in w:
    while len(s) < max_len:
        s += "_"
    res.append(s)
print(res)
