x=[1, 2, 3]
def maps(a):
    l=[]
    for i in a:
        l=l+[i*2]
    return l
#   return [2 * x for x in a]
def newmaps(y):
    return [2*i for i in y]
print(maps(x))
print(newmaps(x))