word = input()
for i in range(int(len(word)/2)):
    if word[i] != (word[-1-i]):
        result = "salah"
        break
    else:
        result = "benar"

print(result)