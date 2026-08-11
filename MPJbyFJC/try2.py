def series_sum(n):
    s=1
    b=0
    for i in range(1,n):
        a=float(1/(1+(3*i)))
        b=b+a
    s=float(s+b)
    round = format(s, ".2f")
    return round
print(series_sum(5))