pos=-1
def bsearch(listy,n):
    l=0
    u=len(listy)-1
    while l<=u:
        m=(l+u)//2
        if listy[m]==n:
            globals()['pos']=m
            return True
        elif listy[m]<n:
            l=m+1
        else:
            u=m-1
lst=[1,2,3,4,6,7,8,10]
n=10
if bsearch(lst,n):
    print("Found at ",pos)
else:
    print("Not Found")