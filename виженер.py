text = input("enter text ")
key = input("enter key ")

result = ""
key_index = 0

for ch in text:
    if ch.isalpha():
        k = key[key_index % len(key)]
        shift = ord(k.lower()) - ord('a')

        code = ord(ch) + shift
        if ch.islower():
            if code > ord('z'):
                code -= 26
        else:
            if code > ord('Z'):
                code -= 26

        result += chr(code)
        key_index += 1
    else:
        result += ch

print("result:", result)
