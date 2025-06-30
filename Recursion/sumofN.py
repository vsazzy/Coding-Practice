def sumofN(n,s):
    if n==0:
        print(s)
        return
    else:
        s=s+n
        sumofN(n-1,s)
        
sumofN(4,0)