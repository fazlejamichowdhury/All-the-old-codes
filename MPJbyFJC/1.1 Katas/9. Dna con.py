def DNA_strand(dna):
    com=''
    for i in dna:
        if i=='A':
            com+='T'
        elif i=='C':
            com+='G'

        elif i=='T':
            com+='A'
        elif i=='G':
            com+='C'
            
    return com
print(DNA_strand('ATTGC'))