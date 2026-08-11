a='asdf'
b=reversed(a)
j=''.join(b)
print(j)

def reverse_words(text):
    s=text.split(' ')
    l=[]
    for i in s:
        l.append(''.join(reversed(i)))
    return ' '.join(l)
print(reverse_words("double  spaces"))