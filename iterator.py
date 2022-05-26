class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()
print(next(values))#once we will get the value it wont be repeated
for i in values:
    print(i)
nums=[11,12,12,13,15]
it=iter(nums)
print(next(it))
for i in nums:
    print(i)