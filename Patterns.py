n=int(input('enter the range for the pattern'))
for i in range(n+1):
    print('#'*i)

eCount=1
while n>0:
    print("*"*eCount)
    eCount+=1
    n-=1



