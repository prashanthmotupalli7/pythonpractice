n=int(input("Enter a given number is armstrong number :"))
sum=0
temp=n
while(temp>0):
    d=temp%10
    sum=sum+d**3
    temp=temp//10
if(sum==n):
    print("given number is armstrong number ")
else:
    print("given number is not armstrong number ")
    