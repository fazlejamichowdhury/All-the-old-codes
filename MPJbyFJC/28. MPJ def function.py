#def function
def mission():
    print("My Programming Journey")
mission()

#argument ***arguments must be defined
def widargmnt(argmnt):
    print(argmnt)
widargmnt('newargmnt')

def double(x):
    print(x*2)
double(2)
double('very good.')

def f(x):
    """ You need a
intendation"""
    print(x+2)
f(10)

def twoArg(x,y):
    print(x+y)
twoArg(3,6)

def even(x):
    if x%2==0:
        print('Nothing left after devision')
    else:
        print('There is a reminder')

even(23)
#return
    
def nsum(x,y):
    return x+y
nsum(2,5) #nothing will be the output
res=nsum(3,4)#you can assign return value

def max(x,y):
    if x>=y:
        return x
    else:
        return y
if (max(5,4)>10):
    print('yes')
else:
    print('it is not.')
    
def shortest_string(x,y):
    if len(x)<=len(y):
        return x
        print('three inteded line')
    else:
        return y
print(shortest_string('assadf','asdf'))

#one function can only return once.use list for multiple value.
def newdouble(a,b):
    return [a*2, b*2]
    
twodo=newdouble(2,5)
print(twodo)