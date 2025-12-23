a = input()
b = input()

if len(a) != len(b):
    print("NO")
else:
    ok = True
    for ch in a:
        if a.count(ch) != b.count(ch):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")
