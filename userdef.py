'''
def getName () :
    print("hello!")

getName()
getName()
getName()
getName()
'''
'''
def detName(name="Luxshi") :
    print(f"My name is {name}")
detName("Jenothan")
detName("Ram")
detName("Vaishnavi")
detName("Ramya")
detName()
'''
'''
def FullName(fname="Srirangan", lname="Sarangan") :
    print(f"Full Name : {fname} {lname}")
    
FullName("Esan")
FullName()
'''
def FullName(fname="Srirangan", lname="Sarangan") :
    print(f"Full Name : {fname} {lname}")
    return fname+" "+lname
    
fullname=FullName(lname="Esan")
print(fullname)