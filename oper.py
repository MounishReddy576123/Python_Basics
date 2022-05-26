from numpy import *
arr=array([2,1,3,5,4])
arr1=arange(1,10,3)
print((arr.all()))
print(sum(arr
))
print(sorted(arr))
print(min(arr))
print(max(arr))
print(arr.cumsum())
print(arr.dtype)
print(concatenate([arr,arr1]))

arr3=arr.view()
arr4=arr.copy()
arr[1]=34
print(arr4)
print(arr3)
print(id(arr3))