inp = open('words.txt')
dic = {}
for line in inp :
    line = line.rstrip()
    words = line.split()
    for word in words:
        if not word in dic:
            temp = {word:''}
            dic.update(temp)
print(dic)
