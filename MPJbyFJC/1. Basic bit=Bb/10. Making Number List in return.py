def count_by(x, n):
    return [i*x for i in range(1,n+1)] #shortest way
""" My solution:
    a=[]
    for i in range(n):
        a.append((i+1)*x)
    return a"""

        
print(count_by(2,10))