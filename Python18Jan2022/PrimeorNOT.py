n=int(input("Enter a number to print prime numbers :"))
count=0
for i in range(2,n):
    if n%i==0:
        count=count+1
if count>1:
    print("Not prime")
else:
    print("Prime")
    