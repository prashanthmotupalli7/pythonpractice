#WAP to find number of occurences of number in list 
count=0
l=[23,45,56,23,23,90]
n=int(input("Enter a number :"))
for i in l:
    if n==i:
        count=count+1
if count!=0:
    print("element present in the list")
    print("The number of occurences of given number",count)
else:
    print("No")