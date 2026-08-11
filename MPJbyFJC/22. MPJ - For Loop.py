thelist=['My','Programming','Journey']

for word in thelist :
    print('*'+word+'*')

name= 'My Programming Journey'
count=0
for letters in name:
    if letters =='r':
        count+=1
print(count)

text='some texts'
for x in text:
    if x=='t':
        break
    print(x)

for x in text:
    if x=='t':
        continue
    print(x)

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

sum=0

for i in x:
    sum+=i
print(sum)