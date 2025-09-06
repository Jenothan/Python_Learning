MonthSalary=[10000, 100000, 150000, 200000, 60000, 70000, 80000, 100000, 300000, 320000, 260000, 90000]
Months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Tax=[]
x=0
YearTax=0
YearSalary=0
YearNetSalary=0
print("-"*67)
print(f"{'Month':<12} | {'Salary':>15} | {'Tax':>15} | {'NetSalary':>15}|")
print("-"*67)
for salary in MonthSalary:
    if salary<50000:
        Mtax=salary*0.03
    elif salary>=50000 and salary<100000:
        Mtax=salary*0.05
    elif salary>=100000 and salary<300000:
        Mtax=salary*0.08
    elif salary>=300000:
        Mtax=salary*0.1
            
    Tax.append(Mtax)
        
    MNetsalary=salary-Mtax
    YearSalary+=salary
    YearNetSalary+=MNetsalary
    YearTax+=Mtax
        
    print(f"{Months[x]:<12} | {salary:>15} | {Mtax:>15} | {MNetsalary:>15}|")
    x+=1
    
print("-"*67)
print(f"{'Total':<12} | {YearSalary:>15} | {YearTax:>15} | {YearNetSalary:>15}|")
print("-"*67)
print()
print(Tax)