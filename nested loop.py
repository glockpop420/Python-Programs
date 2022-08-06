list1=[1,2,3,4,5,6,7]
list5=[10,20,30,40,50,60,70]
L1=len(list1)
dict1={'a':1,'b':2,'c':3}
print(dict1)

list2=[]
list2.append(list1[1:4])
print(list2)



list3=[[1,2,3],[4,5,6],[7,8,9]]
list4=[[10,20,30],[40,50,60],[70,80,90]]
temp1=list3[1][0]+list4[1][2]
print(temp1)

#nested for loop
print(list3[0][1])
for i in range(3):
    for j in range(3):
        temp2=list3[i][j]+list4[i][j]
        print(temp2)

 




        
        

    
