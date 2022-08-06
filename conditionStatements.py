a=3
b=2
c=7
dict1={'K1':[1,2,3],'K2':[10,20,30],'K3':[100,200,300]}
print(dict1['K3'])
print(dict1['K3',0])
#if condition 1: (and or or)(1:always true)(0:always false)
#   statement 1
#   statement 2
#   statement 3
#else:
#   statement 4
#   statement 5
print(a>b)
print(a<b)
if (c>a):   
    print('c is greater than a')
elif(c>b):   
    print('c is greater than b')
elif (c>(a+b)):
    print('c is greater than a+b')
else:
    print('c is not greater than a or b')

