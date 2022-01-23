n=int(input("Enter a number to check weather a given number is strong or not : "))
sum=0
temp=n
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if sum==temp:
    print("Given number is strog number :")
else:
    print("Given number is not strong number :")