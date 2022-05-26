def fib(n):
    a=0
    b=1
    if n>0:
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                if c>n:
                    break
                else:
                    print(c)
                    a = b
                    b = c
    else:
        print("You have entered the wrong choice")
x=int(input("Enter the range for fibonacci series"))
fib(x)


