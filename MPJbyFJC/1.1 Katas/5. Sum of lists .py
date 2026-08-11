def sum_array(arr):
    
    try:
        if len(arr)>2:
            sum=0
            l=list(arr)
            for i in l:
                sum=sum+i
            return sum-max(arr)-min(arr)
        else:
            return 0
    except:
        return 0
print(sum_array([6, 0, 1, 10, 10]))

#print(max([6, 0, 1, 10, 10]), 17))