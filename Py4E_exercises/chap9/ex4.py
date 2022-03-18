inp = input('Enter file name: ')
fhead = open(inp)
address = {}
for line in fhead:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        word = words[1]
        address[word] = address.get(word,0)+1

# This following is to set an intial value.
# We dont choose 0 as initial because in general -
# 0 may not be the smallest.
values = list(address.values())
maxval = values[1]
maxkey = str()

for key in address:
    if address[key] > maxval:
        maxval = address[key]
        maxkey = key
print(maxkey, maxval)
