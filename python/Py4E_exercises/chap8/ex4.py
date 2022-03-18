inp = input('Enter file: ')
fopen = open(inp)
uniquewords = list()
for line in fopen:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if not word in uniquewords:
            uniquewords = uniquewords + [word]
uniquewords.sort()
print(uniquewords)
