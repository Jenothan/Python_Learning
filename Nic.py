from datetime import date

name=input("Enter your name : ")
age=input("Enter your age : ")
nic = input("Enter your NIC number: ")
#200134500469
nic = nic.strip()
datesM = [31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Gender=0
today=0


if len(nic) == 10 :
    nic="19"+nic[0:9]
    print(nic)


while not(nic.isdigit()) :
    print("Enter valid nic number......!")
    nic = input("Enter your NIC number: ")
    if len(nic) == 10 :
        nic="19"+nic[0:9]
        
            
        
year=nic[0:4]
days=int(nic[4:7])



if days>=500 :
    days-=500
    Gender="Female"
else :
    Gender="Male"
    
    
    
x=0 
for i in datesM :
    x+=1
    if days<=i :
        days=days
        break
    days-=i  
    
    

today = date.today()
print(today) 
date=days
print()
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Gender : {Gender}")
print(f"{year}-{x:02d}-{date:02d}")
