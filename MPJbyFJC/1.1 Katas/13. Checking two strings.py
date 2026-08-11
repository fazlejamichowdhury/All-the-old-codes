def is_isogram(string):
    upstr=string.upper()
    for i in upstr:
        if upstr.count(i)>1:
               return False
        if i==upstr[-1]:
            return True
    return True
#False if string.upper()=='aba'.upper() or string.upper()=='moose'.upper() else True
print(is_isogram("else"))