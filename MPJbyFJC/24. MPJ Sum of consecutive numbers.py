"""
Sum of Consecutive Numbers
No one likes homework, but your math teacher has given
you an assignment to find the sum of the first N numbers.

Let’s save some time by creating a program to do the
calculation for you!

Take a number N as input and output the sum of all
numbers from 1 to N (including N).

Sample Input : 100
Sample Output : 5050
"""

#MPJ
number=int(input("Enter the number: "))

total=0

for i in range (number):
    total+=i
total=total+number
print(total)

#alternative
k=list(range(0,number+1))
print(sum(k))
