#calculate electricity bill

unit=int(input("enter electricity unit:"))
if(unit<=50):
    pay=unit*0.50
    fixcharg=(pay*17)/100
    bill=pay+fixcharg
    print("bill for 1st 50 unit is:",bill)
elif(unit<=150):
    pay=(50*0.50)+(unit-50)*0.75
    fixcharg=(pay*17)/100
    bill=pay+fixcharg
    print("bill for 1st 50 unit is:",bill)
elif(unit<=250):
    pay=(50*0.50)+(150-50)*0.75+(unit-150)*1.25
    fixcharg=(pay*17)/100
    bill=pay+fixcharg
    print("bill for 1st 50 unit is:",bill)
else:
    pay=unit*1.50
    fixcharg=(pay*17)/100
    bill=pay+fixcharg
    print("bill for 1st 50 unit is:",bill)