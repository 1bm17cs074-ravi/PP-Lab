def divisor(n):
    i=1
    while i<=(n/2+1):
        if(n%i==0):
            print (i)
        i=i+1
    print(n)
n=int(input('enter number'))
divisor(n)
