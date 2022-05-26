import numpy as np
# Ways of creating an array
#Traditional way
arr=np.array([1,2,3,4,5])
#using linspace()
# here the first two parametrs specify the start and stop values
#the third value specifies the no of parts that the range is divided into by default it is 50
arr1=np.linspace(0,15,3)
print(arr1)
'''using log space we can create an array but it divides th parts based on logerithmic values
it takes the  index from 10 power start to 10 power end and divide the parts'''
arr2=np.logspace(1,50,5)
print(arr2)
arr3=np.arange(1,10,2)# works same as range
arr4=np.zeros(5,dtype=int)
arr5=np.ones([2,4])
print(arr5)