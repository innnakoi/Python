with open(r"C:\Users\zkayd\Desktop\py\1\charles.txt", "r") as file:
    text = file.read()

lines = text.split("\n")
words = text.lower().replace(".", "").replace(",", "").split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

with open("analysis.txt", "w") as file:
    file.write("Lines: " + str(len(lines)) + "\n")
    file.write("Words: " + str(len(words)) + "\n")
    file.write("Frequency: " + "\n")

    for word in word_count:
        file.write(word + ": " + str(word_count[word]) + "\n")
