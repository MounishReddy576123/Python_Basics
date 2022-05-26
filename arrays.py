from array import *
arr=array('i',[])
n=int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("enter the element"))
    arr.append((x))
print(arr)
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[i]:
            arr[j],arr[i]=arr[i],arr[j]
print(arr)


