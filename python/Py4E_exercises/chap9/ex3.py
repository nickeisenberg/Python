inp = input('Enter file name: ')
fhead = open(inp)
address = {}
for line in fhead:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        word = words[1]
        address[word] = address.get(word,0)+1
print(address)
