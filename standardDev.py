import math
x=[9,1,12,11,0,15,8,4,2,11,11,0,6,11,15,1,15,7,11,24,6,7,2,9,8]
y=len(x)
print(y)
sum=0
for i in range(y):
    sum+=x[i]
print(sum)
X=sum/y
Diff=[]
for i in range(y):
    Diff.insert(i,(x[i]-X)**3)
print(Diff)
sum1=0
for i in range(0,y-1):
    sum1+=Diff[i]
print(sum1)
Den=sum1/y
sDiff=[]
for i in range(y):
    sDiff.insert(i,(x[i]-X)**2)
sum2=0
for i in range(y):
    sum2+=sDiff[i]
s=math.sqrt(sum2/(y-1))
skewness=Den/(s**3)
print(skewness)
    
    
