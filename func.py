def add(a,b=6):       # here a,b are called formal arguments
    c=a+b
    print(c)
add(5) # here they are called actual arguments ##Default
print(10<<2)
## four kinds of actual arguments exists
# Positional, Keyword, Default,
def person(name,age):
    print(name +"is " +str(age))
person('Mounish',22)# positional
person(age=28,name="Mounish")#Keyword
## Variable length arguments
def sum(a,*b):
    c=a
    for i in b:
        c+=i
    print(c)
sum(12,14,1,6,17)


def team(*members, **features):
    for member in members:
        print(member)

    for key, value in features.items():
        print("{}: {}".format(key, value))
team("Abena", "Marilyn", Name="FemCode", Project="Edpresso", Number="Two Members")##keyword arguments

