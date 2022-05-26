'''class Car:
    #class variable
    wheels = 4
    def __init__(self):
        self.mil=10  ##instance variables
        self.company="BMW"
c1=Car()
c2=Car()
Car.wheels=5
print(c1.wheels)
print(c2.wheels)'''

class Student:

    school='Telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        #instance method because it works with the objects
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        #Acessors
        return self.m1
    def set_m1(self,value):
        #Mutators
        self.m1=value
    @classmethod
    def getSchol(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class")
s1=Student(34,67,89)
s2=Student(45,76,98)
print(s1.avg())
print(Student.getSchol())
Student.info()