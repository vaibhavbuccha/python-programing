#------------------------------------------------------------------------
# WAP to print fabonacci series till the index n
# ---------------------------------------------------------------------

def fabo(n):
    start = 0
    next  = 1
    i = n
    cn = []
    
    while n > 1:
        if(n == i) :
            cn.append(start)
            cn.append(next)
        else:
            d = cn[-1]+cn[-2]
            cn.append(d)
        n=n-1
    print(cn[-1])

n = int(input("enter the index of fabonacci series : "))
fabo(n)