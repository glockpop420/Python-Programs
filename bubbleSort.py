#Ascending Order
unsortedData = [9,1,12,11,0,15,8,4,2,11,11,0,6,11,15,1,15,7,11,24,6,7,2,9,8]
l=len(unsortedData)
for i in range(l-1):
    for j in range(0,l-i-1):
        if unsortedData[j]>unsortedData[j+1]:#for descending just change to <
            unsortedData[j],unsortedData[j+1]=unsortedData[j+1],unsortedData[j]
for i in range(l):
    print(unsortedData[i])


