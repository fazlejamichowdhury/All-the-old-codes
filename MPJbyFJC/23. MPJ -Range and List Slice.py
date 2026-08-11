number=list(range(10))
print(number)

print(list(range(3,8)))

print(list(range(10,21,2)))

#**Important** in 'for' loop no need to use list for 'range'

for i in range(3):
    print('hi')

for x in range(0,10,2):
    print(x)
    
#list slice
squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[2:4])
print(squares[3:8])
print(squares[0:1])
print(squares[:4])
print(squares[2:])
print(squares[0:-1])

#for backwards= from high to low and negative step
print(squares[8:1:-2])
print(squares[::-1])

#output the last item
print(squares[-1])

"""Write a program that takes a string as input and
outputs the last character of that string"""

a=str(input("Enter the word: "))
print(a[-1])
