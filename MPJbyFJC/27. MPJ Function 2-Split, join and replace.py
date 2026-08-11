#string formating
nums=[4,5,6]
msg="Number: {0} {1} {2}". format(nums[0],nums[1],nums[2])
print(msg)
print("{0}{1}{0}".format("abra", "cad"))

a="{x},{y}".format(x=5,y=12)
print(a)
#join() turns list into strings
x=" ".join(["My","Life"])
print(x)

#**split()**this function turns string into list with seperator

splitting="My Programming Journey"
x=splitting.split(' ')
print(x)

#string.replace('previous','new')
x='My life'
print(x.replace('My','Our'))

#.lower() and .uper()
print('this is a sentence'.upper())
print('ALL CAPS SENTENCE CHANGE'.lower())
