msg = int(input('>'))
key = {
    range(0, 11): 'you are beginner',
    range(11, 21): 'you are almost eligible',
    range(21, 31): 'you are an very close',
    range(31, 41): 'you are done'
}
output = ""
for word in msg:
    output += key.get(word, word)
print(output)
