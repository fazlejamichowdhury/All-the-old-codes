'''You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years of age, the ticket is free.

Your program needs to take the ages of 5 passengers as input and
output the total price for their tickets.

Sample Input
18
24
2
5
42'''

total=0
i=0
while i<5:
    i+=1
    a=int(input("Enter the age: "))
    if a<3 and a>0:
        continue
    total+=100

print(total)
    