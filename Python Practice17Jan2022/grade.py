#WAP to find a grade and print total number
project_marks=int(input("Enter your project marks : "))
internal_marks=int(input("Enter your internal marks : "))
external_marks=int(input("Enter your external marks : "))
total_marks=0
total_marks=(project_marks*70/100)+(external_marks*20/100)+(internal_marks*10/100)
if project_marks>=50 and internal_marks>=50 and external_marks>=50:
    print("Total Marks :",total_marks)
if project_marks<50:
    print("You failed in project and your marks in project: ",project_marks)
if internal_marks<50:
    print("You failed in internals and your marks in internal is : ",internal_marks)
if external_marks<50:
    print("You failed in externals and your marks in external : ",external_marks)
if total_marks>=90 and internal_marks>=50 and external_marks>=50 and external_marks>=50:
    print("A Grade")
if total_marks>=75 and total_marks<90 and internal_marks>=50 and external_marks>=50 and project_marks>=50:
    print("B Grade")
if total_marks>=50 and total_marks<75 and internal_marks>=50 and external_marks>=50 and project_marks>=50:
    print("C Grade")
