p=int(input("Enter a principle amount :"))
t=int(input("Enter a time : "))
r=int(input("Enter rate : "))
i=(p*t*r)/100
a=p*(1+r/100)**t
ci=a-p
print("The Simple Intrest :",i)
print("The Compund Intrest : ",ci)

