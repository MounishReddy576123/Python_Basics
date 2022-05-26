"""
ERRORS
1)Compile Time
2)Run Time
3)Logical Error

"""
a=5
b=0
try:
    print("reource open")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey,You cannot divide a number by Zero",e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Something Went Wrong")
finally:
    print("resource Closed")