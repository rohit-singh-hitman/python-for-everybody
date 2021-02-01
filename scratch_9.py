import re
sum=0
l=""
fname = input('enter the file:')
f = open(fname)
for line in f:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x)>0:
        print(x)
        for word in x:

            p=int(word)
            #print(p)
            sum=sum+p
print(sum)


