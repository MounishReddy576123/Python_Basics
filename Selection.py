#using the Selection sort to sort elemnts
def ssort(lst):
    for i in range(len(lst)-1):
        minpos=i
        for j in range(i,len(lst)):
            if lst[j]<lst[minpos]:
                minpos=j
        temp=lst[i]
        lst[i]=lst[minpos]
        lst[minpos]=temp


nums=[2,1,4,3,5,7,5]
ssort(nums)
print(nums)