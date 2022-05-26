from array import *
vals = array('i',[5,3,4,2])
vals.append(1)
newArr=array(vals.typecode,[a for a in vals])
for e in newArr:
    print(e)
