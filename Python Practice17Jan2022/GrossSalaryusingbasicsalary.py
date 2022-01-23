# WAP to accept the basic salary & find gross salary 
basic_salary=float(input("Enter basic salary :"))
DA=(basic_salary*80)/100
HRA=(basic_salary*76)/100
gross_salary = basic_salary+DA+HRA
print("Gross Salary : ",gross_salary)
