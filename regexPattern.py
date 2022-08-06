cherimport re
#s='welcome python'
#print(s)
#print(s[3])
#you cannot modify a string value
#s='Hello Amuthan! Welcome you to python programing'
#s='Hello Amuthan!' + s[0:7] + 'you to ' + s[8:_] + ' programming' 
#print(s)
#s='welcome python'[::-1] print reverse
#a='hi!'
#print(a*4) prints multiple times
#S='a'
#print(ord(S))
#y=ord('a')+1
#print(chr(y)) ascii value back to character
#print('a\nb\tc\a\a\a')/n for space /t for tab


register=input()
if re.match("[1-9][a-e]",register):
    print("Matched")
else:
    print("Unmatched")
if re.match("^[+][9][1][6-9][0-9]{9}$",register):
    print("Matched")
else:
    print("Unmatched")
    
#S="Hello Amuthan, Welcome to Python Course"
#print(S.find('Amuthan'))
#print(S.replace('Amuthan','Nithin'))
#print(S)
#S_split=S.split(',')
#print(S_split)

#S="India is my Country. Our national flag have three colours. They are Saffron colour, white colour and green colour. India got independence in 1947. Many government organizations and private NGO organizations are working day and night for the growth of our Country."

##S="welcome to python course"
##list1=[i for i in S]
##print(list1)
