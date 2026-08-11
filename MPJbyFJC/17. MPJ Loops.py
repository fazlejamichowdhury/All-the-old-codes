i=1
while i<5:
    print(i)
    i=i+2
    print("Finished!")
print("Last finish")

x=0
while x<3:
    print(x)
    x+=1
sum=0
a=10
while a>0:
    sum+=a
    a-=1
print(sum)

w=1
while w<10:
    if w%2==0:
        print(w,"is even.")
    else:
        print(w,"is odd.")
    w+=1
q=0
while True:
    print(q)
    q=q+1
    if q>=5:
        print("Breaking")
        break
print("breaking done")

s=0
while s<5:
    s+=1
    if s==3:
        print("Skipping")
        continue
    print(s)