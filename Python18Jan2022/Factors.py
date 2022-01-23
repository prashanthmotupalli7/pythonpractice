#wap to find number of factors of given number
n=int(input("Enter a number to find Factors: "))
count=[]
for i in range(1,n+1):
    if n%i==0:
      print(i)
