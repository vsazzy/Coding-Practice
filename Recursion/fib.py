def fib(n):
    if n<=1:
        return n
    else:
        x=fib(n-1)
        y=fib(n-2)
        return x+y           

print(fib(5))
