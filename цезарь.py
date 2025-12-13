text = input("enter text ")
shift = int(input("enter move number"))

result = ""

for ch in text:
    if ch.isalpha():
        code = ord(ch) + shift
        if ch.islower():
            if code > ord('z'):
                code -= 26
        else:
            if code > ord('Z'):
                code -= 26
        result += chr(code)
    else:
        result += ch

print("Результат:", result)
