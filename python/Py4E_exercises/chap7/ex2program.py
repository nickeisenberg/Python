inp = input('Enter the the file: ')
count = 0
total =0
try:
  fname = open(inp)
except:
  print('File not found')
  exit()
for i in fname:
 pos = i.find('X-DSPAM-Confidence:')
 if pos == -1: continue
 count = count + 1
 beg = i.find(' ', pos)
 end = i.find('\n', beg)
 val = float(i[beg+1:end])
 total = total + val
print(total / count)
