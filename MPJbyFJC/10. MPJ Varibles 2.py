#working with variables
x=7
print(x)

print(x+3)
print(x)

y=123.456
print(y)

age = 23
age = 23-6
print(age)

a= 8
name ="Bob"
print(a*name)

z=32
print(z)
del z

spam=2
eggs=3
del spam
eggs=4
spam=5
print(spam*eggs)

num = 7
print(num**3)

#taking user input
writit=input()
print(writit)
#Even if the user enters a number as input, it's processed as a string
writit2=input()
print("You entered: "+writit2)

#coverting the input to integer
age=int(input())
print(age)

a='2'
b='3'
c=int(a)+int(b)
#coverting to float
height= float(input())
print(height)

#str() function, which converts a number to a string
age=42
print("His age is "+str(age))

#in place operators
k=k+3
k+=2
k-=3
k*=5

miles=int(input())
km=miles*1.60934
print(km)