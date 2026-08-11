l=[1, 2, 3, 4, 5]
def multiplySeries(items):
    series=''
    result=1
    for i in items:
        result*=i
        
        if i==items[-1]:
            series=series+' '+str(i)+' ='+' '+str(result)
            break
        series=series+' '+str(i)+' *'
    return series
print(multiplySeries(l))