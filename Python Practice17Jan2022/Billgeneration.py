#WAP to accept 3 numbers & find max number
#Wap to accept units from user and find bill
#for first 50 units the charges are 0.75p/u
#for next 100 units the charges are 2.10p/u
#above 250units the charges are :2.80p/u

units=int(input("Enter units : "))
bill=0
if units<=50:
    bill=units*0.75;
elif units<=150:
     bill=(50*0.75)+(units-50)*2.10
elif units<=250:
    bill=(50*0.75)+(100*2.10)+(units-150)*2.50
else:
    bill=(50*0.75)+(100*2.10)+(100*2.50)+(units-250)*2.80
print("Bill :",bill)
gst=(bill*10)/100
print("GST : ",gst)
bill=bill+gst
print("Final Bill : ",bill)