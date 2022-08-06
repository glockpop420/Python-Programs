dict1={'101A':['Brown rice',50,42.50,41.25],
       '102B':['Whole Wheat',30,27.45,21.50],
       '102C':['Tomato Suace',25.50,20.25,18.70],
       '103D':['Mustard',40,39.45,37],
       '104E':['Barbeque Sauce',45,43,41.50],
       '105F':['Red Wine Vinegar',4000,3800,3750],
       '106G':['Salsa',200,189.50,170],
       '107H':['Extra Virgin Olive Oil',500,478.50,455.70],
       '108I':['Canola Oil',200,180,118],
       '109J':['Hot Pepper Sauce',100,98.50,91.25],
       '110K':['Bananas',60,55,50],
       '111L':['Apples',300,250,120],
       '112M':['Oranges',200,140,110],
       '113N':['Mangoes',100,80,50],
       '114O':['Strawberries',100,90,80],
       '115P':['Blueberries',95,80,75],
       '116Q':['Green Teas',250,225,200],
       '117R':['Sparkling Water',20,14.50,11],
       '118S':['Dried Apricots',270,250,230],
       '119T':['Dried Figs',100,95,90],
       '120U':['Dried Prunes',90,85,80],
       '121V':['Almonds',900,870,850],
       '122W':['Cashews',100,950,910],
       '123X':['Walnuts',800,770,720],
       '124Y':['Peanuts',400,380,360],
       '125Q':['Pecans',350,320,300],
       '201A':['Pistachios',1200,1180,1160],
       '202B':['Sunflower Seeds',150,112.50,103.45],
       '203C':['Sesame Seeds',120.50,110.25,101.40],
       '204D':['Whole Flaxseeds',95.20,90.45,89.20]}
dict2={'AAA1001':['Surian',9500012345],
       'AAA1002':['Nila',9500023456],
       'AAA1003':['Arivazhagan',9712300078],
       'AAA1004':['Nitin Kumar',9586233333],
       'AAA1005':['Aravind',6931245872],}
name=input('Enter name of the customer : ')
num=float(input('Enter number of the customer : '))

if (num==(dict2['AAA1001'][1])):
    print('Registered Customer')
    r=1
elif (num==(dict2['AAA1002'][1])):
    print('Registered Customer')
    r=1
elif (num==(dict2['AAA1003'][1])):
    print('Registered Customer')
    r=1
elif (num==(dict2['AAA1004'][1])):
    print('Registered Customer')
    r=1
elif (num==(dict2['AAA1005'][1])):
    print('Registered Customer')
    r=1
else:
    print('Not a Registered Customer')
    r=0
print(dict1['125Q'])
print(r)
amt=float(0)

for i in range(2):
    code=input('Enter code of the product : ')
    if code in dict1.keys():
        quality=input('Enter quality of the product : ')
        if quality=='1':
            quantity=input('Enter quantity of the product : ')
            amt=quantity*(dict1[code][1])
        elif quality=='2':
            quantity=input('Enter quantity of the product : ')
            amt=quantity*(dict1[code][2])
        elif quality=='3':
            quantity=input('Enter quantity of the product : ')
            amt=quantity*(dict1[code][3])
        else:
            print('Invalid Quality, please use 1,2 or 3')
    else:
        print('Invalid code, please try again')

print(amt)
if r==1

        
            
    


    
    
    
    
