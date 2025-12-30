s = input("Enter string: ")

words = s.split()     
result = ""

for word in words:
    letters = list(word)   
    letters.sort()         
    sorted_word = "".join(letters)
    result = result + sorted_word + " "

print(result)
