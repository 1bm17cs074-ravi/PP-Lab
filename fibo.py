def fib(n):
    if n==0:
        return 1
    else:
        return n*fib(n-1)
n = int(input())
print(fib(n))