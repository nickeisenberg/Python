inp = input('Enter a file: ')
fhand = open(inp)
import re
data = list()
for line in fhand:
    line = line.rstrip()
    xstr = re.findall('New Revision: ([0-9.]+)', line)
    if len(xstr) > 0:
        for x in xstr:
            data.append(float(x))
count = 0
sum = 0
for x in data:
    sum = sum + x
    count = count+ 1
avg = sum/count
print(int(round(avg,0)))
