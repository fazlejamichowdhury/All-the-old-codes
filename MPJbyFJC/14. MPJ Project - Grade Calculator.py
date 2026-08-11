#MPJ Project : Grade calculator
mark=int(input("Enter the Mark: "))
if 0<=mark<50:
    print("Fail")
elif 100>=mark>50:
    print("Passed")
else:
    print("Enter a correct Mark")