class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __abs__(self):
        m1=abs(self.m1)
        m2=abs(self.m1)
        s5=Student(m1,m2)
        return s5
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+self.m2
        if r1 >r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
s1=Student(25,45)
s2=Student(45,55)
s3=s1+s2
s4=Student(-895,-65)
s5=abs(s4)
print(s3.m1)
print(s5.m1)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s1)##Normally by defalut __str__ method is called to print the value here we are overloading the opearator


