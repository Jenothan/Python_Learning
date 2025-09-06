waterUnit = input("Enter the water unit.. : ")
waterUnit = int (waterUnit)
payment = 0

if waterUnit > 0 :
    if waterUnit >= 1 and waterUnit <= 1000 :
        payment = 500
    elif waterUnit >= 1001 and waterUnit <= 3000 :
        payment = (waterUnit - 1000) * 3 + 500
    elif waterUnit >= 3001 and waterUnit <= 10000 :
        payment = (waterUnit - 3000) * 5 + 2000 * 3 + 500
    else :
        payment = (waterUnit - 10000) * 7 + 7000 * 5 + 2000 * 3 + 500
else :
    print("Invalid Water Unit")

print(payment)