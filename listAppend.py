def inputL():
  l_in = []
  for i in range(15):
    n = int(input())
    l_in.append(n)
  return l_in
def Freq_Count(listA):
    dict1 = {}
    n=len(listA)
    for i in range(0,n,1):
        c=0
        for j in range(i,n,1):
            if listA[j]==listA[i]:
                c+=1
        dict1[i] = c
    print(dict1)
L = inputL()
Freq_Count(L) 
            
