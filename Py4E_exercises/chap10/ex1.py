inp = input('Enter a file name: ')
fhead = open(inp)
counts = {}
for line in fhead:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0)+1
bigsmall = list()
for key,val in counts.items():
    bigsmall.append((val,key))
bigsmall.sort(reverse = True)
for val, key in bigsmall[:1]:
    print(val,key)
