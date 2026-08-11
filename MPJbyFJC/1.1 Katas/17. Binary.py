# Use this for user input
#decNum = int(input("Enter any Decimal Number: "))
 
decNum = 4785
print(bin(decNum)[2:])
 
decNum1 = 10
print(bin(decNum1)[2:])
 
decNum2 = 345
print(bin(decNum2)[2:])

def add_binary(a,b):
    return bin(a+b)[2:]