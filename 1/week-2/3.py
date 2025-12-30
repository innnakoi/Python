s = input()

left = s[0]
sign = s[1]
right = s[2]
result = int(s[4:])  

if left == 'x':
    if sign == '+':
        x = result - int(right)
    else:  
        x = result + int(right)

elif right == 'x':
    if sign == '+':
        x = result - int(left)
    else:
        x = int(left) - result

else:  
    if sign == '+':
        x = int(left) + int(right)
    else:
        x = int(left) - int(right)

print(x)
