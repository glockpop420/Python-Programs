# Python program to check if the number is an Armstrong number or not
num = int(input("Enter a number: "))

# find the sum of the cube of each digit
def fas(x):
   order = len(str(x))
   sum = 0
   temp = x
   while temp > 0:
      digit = temp % 10
      sum += digit ** order
      temp //= 10
   return sum
sum=fas(num)
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

    

