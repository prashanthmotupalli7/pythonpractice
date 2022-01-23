n=int(input("Enter a nunmber :"))
sum=0
while(n>0):
    d=n%10
    sum=sum+d
    n=n//10
    
print("the output is",sum)