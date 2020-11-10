f = open('input.txt')
str1 = int(f.readline())
str2 = f.readline()
str2 = str2.split(' ')
str2 = list(str2)
str2 = [int(i) for i in str2]
ln1 = []
ln2 = []
for i in str2:
    if i % 2 == 0:
        ln1.append(i)
    else:
        ln2.append(i)
ln1 = [str(i) for i in ln1]
ln2 = [str(i) for i in ln2]
if len(ln1) > len(ln2):
    c = 'Yes'
else:
    c = 'No' 
res1 = ' '.join(ln2)
res2 = ' '.join(ln1)
suka = [res1, res2, c]
zaebalsa = '\n'.join(suka)
with open('output.txt','w') as f:
    f.write(zaebalsa)         


       


