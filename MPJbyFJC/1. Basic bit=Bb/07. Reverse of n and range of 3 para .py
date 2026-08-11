def digitize(n):
    st=str(n)
    l=list(st)
    r=reversed(l)
    ns=''.join(r)
    nl=[int(x) for x in ns]
    return nl

"""
def digitize(n):
    return [int(x) for x in str(n)[::-1]]"""

print(digitize(534523))

def reverse_seq(n):
    return [x+1 for x in range(n)[::-1]]
   # return list(range(n,0,-1))#range(start,end,step)
print(reverse_seq(5))
