#WAP to accept salary and 3 shopping bills
#1 total shopping amount
# how much percentage of his salary he spent on shopping

salary=float(input('Enter your salary :'))
shoppingbill1=float(input('Enter shopping bill 1 : '))
shoppingbill2=float(input('Enter shopping bill 2 : '))
shoppingbill3=float(input('Enter shopping bill 3: '))

total=shoppingbill1+shoppingbill2+shoppingbill3

salaryspent=(total*100)/salary
print("total shoping ammount : ",total)
print(salaryspent,"% amount spent from salary")

