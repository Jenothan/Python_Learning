salarys=[]
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


i=0
while i<12:
    Monthsalary=input(f"Enter your {months[i]} month salary : ")
    while not(Monthsalary.isdigit()):
       print('Please enter valid Salary')
       Monthsalary=input(f"Enter your {months[i]} month salary : ")
    salarys.append(int(Monthsalary))
    i+=1
def calcTax():
    x=0
    Ytax=0
    Ysalary=0
    Ybalsalary=0
    print(f"{'Month':<12} {'Salary':<18} {'Tax':<24} {'NetSalary'}:<30")
    for salary in salarys:
        if salary<50000:
            Mtax=salary*0.03
        elif salary>=50000 and salary<100000:
            Mtax=salary*0.05
        elif salary>=100000 and salary<300000:
            Mtax=salary*0.08
        elif salary>=300000:
            Mtax=salary*0.1
        
        
        Mbalsalary=salary-Mtax
        Ytax+=Mtax
        Ysalary+=salary
        Ybalsalary+=Mbalsalary
        
        
        print(f"{months[x]:<12} {salary:<18} {Mtax:<24} {Mbalsalary:<30}")
        x+=1
    print(f"{'Total':<12} {Ysalary:<18} {Ytax:<24} {Ybalsalary:<30}")

calcTax()