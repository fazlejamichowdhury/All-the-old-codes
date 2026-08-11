def first_non_consecutive(arr):
    for i in arr: 
        if i != arr[0]:
            if i != arr[(arr.index(i)-1)]+1:
                return i

print(first_non_consecutive([-5,-4,-3,-1]))