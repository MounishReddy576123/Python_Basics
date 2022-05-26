'''def fact(n):
    c=1
    for i in range(1,n+1):
        c*=i
    return c
x=int(input("enter the number for finding  factorial"))
k=fact(x)
print(k)'''
## Recursion
#Function calling by itself
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
x=int(input("enter the number for finding  factorial"))
k=fact(x)
print(k)
