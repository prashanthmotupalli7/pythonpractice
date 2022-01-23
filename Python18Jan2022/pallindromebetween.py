#wap to print pallindrome numbers between 50 - 500
m=int(input("Enter a start number :"))
n=int(input("Enter a end number :"))

for i in range(m,n+1):
    temp=i
    rev=0
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
        if i==rev:
            print(i,end=" ")
             