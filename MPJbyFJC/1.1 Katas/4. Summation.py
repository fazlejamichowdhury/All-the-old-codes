def summation(num):
    sum=0
    for i in range(num):
        print(i)
        sum+=i+1
    return sum
#    return sum(range(1,num+1))

print(summation(5))