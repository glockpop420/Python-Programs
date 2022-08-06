#function definitions
#def function name(arg1,arg2,arg3,.....)
def arith_fun(x,y):
    print('Start of function')
    z1=x+y
    z2=x-y
    z3=x*y
    z4=x/y
    z=[z1,z2,z3,z4]
    print('Processed output z:',z)
    print ('end of function')
    return z#return value
a=5
b=2
#c=a+b
c=arith_fun(a,b)#number of arguments should be the same as the main function
print ('c:',c)
d=50
e=20
f=d+e
print ('f:',f)
g=500
h=200
i=g+h
print ('i:',i)
