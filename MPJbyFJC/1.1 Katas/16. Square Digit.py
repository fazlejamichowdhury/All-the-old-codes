def square_digits(num):
    s=str(num)
    ns=''
    a=0
    for i in s:
        a=int(i)*int(i)
        ns+=str(a)
    return int(ns)
        
print(square_digits(239))