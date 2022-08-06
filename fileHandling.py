import csv
#File Inputs
InputObj=open('C:/Users/prana/OneDrive/Computer/Python Programs/input.csv','r')
ValuesObj=csv.reader(InputObj)

Inputs=list(enumerate(ValuesObj))
print(Inputs)

InputObj.close()
print(Inputs[3][1])
#Process
InputList1=Inputs[0][1]
print(InputList1)
InputList2=Inputs[2][1]
print(InputList2)

a=float(InputList1[0])
b=float(InputList2[1])
print(a)
print(b)
c=a+b
print(c)

OutputList=[]
OutputList.append(c)
OutputObj=open('C:/Users/prana/OneDrive/Computer/Python Programs/output.csv','w')
write=csv.writer(OutputObj)
write.writerow(OutputList)
OutputObj.close()
