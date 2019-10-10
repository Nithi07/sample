message = input('>')
num = {
    "1": "0ne",
    "2": 'Two'
}
output = ""
for word in message:
    output += num.get(word, word)
print(output)