def dirReduc(arr):
    larr=len(arr)
    az=1
    while az<larr :
        az+=1
        arr=' '.join(arr).upper()
        a=['NORTH SOUTH','SOUTH NORTH','EAST WEST','WEST EAST']
        for i in range(len(arr)):
            for i in a:
                if i in arr:
                    arr=arr.replace(i,'')
                    
        
        arr=arr.split(' ')
        
        for i in arr:
            if i=='':
                arr.remove('')
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))