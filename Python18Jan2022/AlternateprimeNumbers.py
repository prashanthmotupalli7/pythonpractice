# Python program to display all the prime numbers within an interval

lower = int(input("Enter a lower number: "))
upper = int(input("Enter a upper number:"))

print("Prime numbers between", lower, "and", upper, "are:")
count=0
a=0
for num in range(lower, upper + 1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
                break
       else:
           a=a+1
           if(a%2==0):
               print(num)