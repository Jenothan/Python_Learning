salary=[]
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
netsalary=0
netTax=0
netOriginalSalary=0
i=0
x=0
monthtax=0
while x<12 :
   Monthsalary=input(f"Enter your {x+1} month salary : ")
   salary.append(int(Monthsalary))
   x+=1

while i<len(salary):
    if salary[i]<50000:
        monthtax=salary[i]*0.03
    elif salary[i]>=50000 and salary[i]<100000:
        monthtax=salary[i]*0.05
    elif salary[i]>=100000 and salary[i]<300000:
        monthtax=salary[i]*0.08
    elif salary[i]>=300000:
        monthtax=salary[i]*0.1
    monthsalary=salary[i]-monthtax
    print(f"{months[i]} salary is {salary[i]}")
    print(f"{months[i]} Tax is {monthtax}")
    print(f"{months[i]} balance salary is {monthsalary}")
    netsalary+=salary[i]
    netTax+=monthtax
    netOriginalSalary+=monthsalary
    print()
    i+=1
print(f"*******************Yearly salary : {netsalary}************************")
print(f"*******************Yearly tax : {netTax}******************************")
print(f"*******************Yearly balance salary : {netOriginalSalary}********")