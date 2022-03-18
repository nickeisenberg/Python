inp = input('name of file: ')
fhand = open(inp)
count={}
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        day = words[2]
        count[day] = count.get(day,0)+1
print(count)
