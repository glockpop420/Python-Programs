#subtract all the values of x with mean of x and vice versa in the numerator
#multiply both
#the value of xi-(mean of x) should be squared in the denominator

def mean(num):
    length=len(num)
    sum=0
    for i in range(length):
        sum+=num[i]
    sum/=length
    return sum
        

def slope(num1,num2):
    length1=len(num1)
    length2=len(num2)
    mx=mean(num1)
    my=mean(num2)
    sum1=0
    sum2=0
    for i in range(length1): 
        sum1 += (num1[i]-mx)*(num2[i] - my)
    for i in range(length1): 
        sum2 += (num2[i] - mx)**2
    s = sum1/sum2
    return s
x = []
y = []
for i in range(25):
    x.append(int(input()))
for i in range(25):
    y.append(int(input()))
a=slope(x,y)
print(a)
