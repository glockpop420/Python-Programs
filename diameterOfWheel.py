import math
def area(x,y):
    a=float(round(2*math.pi*x*y,2))
    return a
def conversion(b):
    conv=float(round(b*6.4516,2))
    return conv
dict1={'1':[15,6],
       '2':[16,7],
       '3':[17,8],
       '4':[18,9]}
print('1-15 inches')
print('2-16 inches')
print('3-17 inches')
print('4-18 inches')
n=input('enter which diameter you would for your wheel like using the numbers given above: ')
if n in dict1.keys():
    a=float(dict1[n][0]/2)
    b=dict1[n][1]
    c=area(a,b)
    d=conversion(c)
    print('Paid ',d,' Dollars')
    dict2={d:[a,b],c:[a,b],d:[a,b]}
    print(dict2)
else:
    print("Invalid Input")


    
    
