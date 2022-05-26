class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 is Working")
    def feature2(self):
        print("Feature 2 is Working")
class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature3(self):
        print("Feature 3 is Working")

    def feature4(self):
        print("Feature 4 is Working")
    #single level inheritence
class C(B):
    def feature5(self):
        print("Feature 5 is Working")

    def feature6(self):
        print("Feature 6 is Working")
    #Multilevel Inheritence
class D:
    def __init__(self):
        print("in D init")
    def feature7(self):
        print("Feature 7 is Working")

    def feature8(self):
        print("Feature 8 is Working")
class E(A,D):
    def __init__(self):
        super().__init__()
        print("in E init")
    def feature9(self):
        print("Feature 9 is Working")
    def feat(self):
        super().feature8()
    #Multiple Inheritence
b=B()# first it will call the init method of classB
b.feature1()
e=E()
e.feat()
# In Multiple Inheritance we will have a concept of Method Resolution Order Which will call methods from left to right

