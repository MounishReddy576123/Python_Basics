pos=-1
def lsearch(list,n):
    for i in list:
        if i==n:
           globals()['pos']=list.index(i)
           return True
    return False
lst=[1,2,3,4,5,6]
n=10
if lsearch(lst,n):
    print("Found at ",pos)
else:
    print("Not Found")

