def abbrev_name(name):
    s=name.split(' ')
    return s[0][0].upper()+'.'+s[1][0].upper()

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

print(abbrevName('Sam Harris'))

a,b= '4 5'.split(' ')
print(b)