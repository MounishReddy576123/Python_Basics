
def sortet(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t
    return nums

num=[3,2,5,7,1,8]
lst=sortet(num)
print(lst)
