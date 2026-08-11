#MPJ Project
"""
You and three friends go to a baseball game and you offer to go to the concession stand for everyone. They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task 
Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format 
You will output a number of the total cost of the food and drinks.

Sample Input 
'Pizza Cheeseburger Water Popcorn'

Sample Output 
26.75
"""

order=input("Enter your order: ")
items=order.split(' ')

total1=0
total2=0
total3=0
total4=0
total5=0

for i in items:
    if i=='Nachos':
        total1=total1+6
    elif i=='Pizza':
        total2=total2+6
    elif i== 'Water':
        total3=total3+4
    elif i=='Cheeseburger':
        total4=total4+10
    else:
        total5=total5+5

total=total1+total2+total3+total4+total5
total+= (total/100)*7
print(total)