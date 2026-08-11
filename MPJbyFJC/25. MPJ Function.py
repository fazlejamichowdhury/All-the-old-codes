#MPJ
#list functions
#len(list)
nums=[1,3,5,2,4]
print(len(nums))
#list.append(item)
nums.append('added')
print(nums)

string=["MY", "Programming", "Journey"]
x=len(string)
print(x)
#list.insert(pos,item)
string.insert(1,"Whole")
print(string)

newnum=[6,2,5,8,2]

newnum.append(4)
newnum.insert(0,2)
print(newnum)
print(len(newnum))
#list.index()
print("Printing Index:")
print(string.index('Journey'))
#max(list) and max(list)
print(max(newnum))
print(min(newnum))
#list.count(item)
newnum.count(2)
#list.remove(item)
newnum.remove(8)
#list.reverse()
newnum.reverse()
print(newnum)

print("last task:")
last_list=[3,6,8,2,6]
last_list.remove(2)
print(len(last_list)+last_list.count(6))