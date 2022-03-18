inp = input('Enter a file name: ')
fhead = open(inp)
counts = {}
for line in fhead:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        word = words[5]
        time = word.split(':')
        hour = time[0]
        counts[hour] = counts.get(hour,0)+1
bigsmall = list()
for key, val in counts.items():
    bigsmall.append((key,val))
bigsmall.sort()
for key, val in bigsmall:
    print(key,val)
