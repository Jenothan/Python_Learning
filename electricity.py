unit = input("Enter the Unit count.. : ")
unit = int(unit)
payment = 0

if unit > 0 :
    if unit >= 1 and unit <= 90 :
        payment = unit * 7
    elif unit >= 91 and unit <= 150 :
        payment = (unit - 90 ) * 10 + 90*7
    elif unit >= 151 and unit <= 300 :
        payment = (unit - 150) * 18 + 90*7 + 60*10
    else :
        payment = (unit - 150) * 18 + 90*7 + 60*10
        payment = payment + payment * 3/100
        payment = f"Added 3% tax for using over 300 unit: Total : {payment}"
    print(f"Your used unit :{unit}\nTotal amount: {payment}")
else :
    print("Invalid Unit")

