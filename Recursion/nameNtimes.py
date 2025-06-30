def printNtimes(n):
    if n>0:
        print("Sunny")
        printNtimes(n-1)
    else:
        return
printNtimes(4)