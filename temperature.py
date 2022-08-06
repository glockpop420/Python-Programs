#IMPLEMENTATION OF SWITCH CASE

switches = {1:["Windows",False], 2:["Ceiling Fan",False], 3:["Air Conditioner",False]}
temp = int(input("Enter the room temperature: "))
if(temp == 22):
    switches[1][1]=False
    switches[2][1]=False
    switches[3][1]=False
    print(switches)
elif(temp >= 24 and temp < 26):
    switches[1][1]=True
    switches[2][1]=False
    switches[3][1]=False
    print(switches)
elif(temp >= 26 and temp < 28):
    switches[1][1]=False
    switches[2][1]=True
    switches[3][1]=False
    print(switches)
elif(temp >= 28):
    switches[3][1]=False
    switches[2][1]=False
    switches[3][1]=True
    print(switches)
else:
    print("Input value limit exceeded")

