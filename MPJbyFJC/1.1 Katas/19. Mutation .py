def remove_smallest(numbers):
    if numbers>[]:
        num=[]
        for i in numbers:
            num.append(i)
        num.remove(min(num))
        return num
    else:
        return []

print(remove_smallest([2,2,1,2,1]))

