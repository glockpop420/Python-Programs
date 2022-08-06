dict1={'a':100,
       'b':200,
       'c':300}
def salary(x,y):
    amount=x*y
    print(amount)
    return amount
a=input('enter the catagory under which you work under:') 
if a in dict1.keys():
    b=input('enter the number of hours you have worked:')
    pr=int(dict1[a])
    s=salary(pr,b)
    dict2={a:[b,s]}
    print(dict2)
else:
    print('Invalid Input')
