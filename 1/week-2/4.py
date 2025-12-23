n, m = map(int, input().split())
s = input()

words = []

for i in range(n - m + 1):
    part = s[i:i+m]
    if part not in words:
        words.append(part)

print(len(words))
