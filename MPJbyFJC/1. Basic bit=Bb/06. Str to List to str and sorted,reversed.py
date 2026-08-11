def Descending_Order(num):
    s = str(num) #to string
    s = list(s) # to list
    print(s)
    s = sorted(s)
    print(s)
    s = reversed(s)
    print(s)
    s = ''.join(s)#converting to string
    print(s)
    return int(s)
print(Descending_Order(5432534))

a= "sohag,safi"
s=a.split(',')
print(s)

j=''.join(s)
print(j)

l1=list(a)
print(l1)
