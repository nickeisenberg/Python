inp = input('Enter a regular expression: ')
fhand = open('mbox.txt')
count = 0
import re
for line in fhand:
    line =  line.rstrip()
    if re.search(inp,line):
        count = count + 1
print(count)
