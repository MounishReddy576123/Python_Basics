'''a = 10
b=20
print(id(a))
def fuun():
    a=9
    x=globals()['a'] ## fetches all the global variables especially useful when we want to have a variable with same global variable name but we want to cahange the global variable
    print(id(x))
    globals()['a']=15
    print("x=",x)
    print("Inside a = ",a)
fuun()
print("Outside a= ",a)'''
x=int(input("Enter the length of the list"))
lst=[]
for i in range(x):
    k=input("Enter the value")
    lst.append(k)
def count(lst):
    c=0
    for i in lst:
        if len(i)>=5:
            c+=1
    return c

e= count(lst)
print("the number of strings with length greater than 5 is ",e)
