#nested list
list1=[1,2,3,4,5,6,7]
list2=[10,20,30,40,50,60,70]
list3=[[1,2,3],[4,5,6],[7,8,9]]
listOut=[]
#listOut.append(list1[0]+list2[0])
#listOut.append(list1[1]+list2[1])
#listOut.append(list1[2]+list2[2])
#listOut.append(list1[3]+list2[3])
#listOut.append(list1[4]+list2[4])
#listOut.append(list1[5]+list2[5])
#listOut.append(list1[6]+list2[6])

print(listOut)

for i in range(7):
    print(i)
    print(list1[i] + list2[i])
    listOut.insert(i,list1[i]+list2[i])
    print("value inserted in the list")
print(listOut)
    
