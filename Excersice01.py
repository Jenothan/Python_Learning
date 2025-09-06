callMin = input("Enter the call min: ")
callMin = int(callMin)

charge = 0

if callMin>=1 and callMin<=30 :
    charge = callMin * 2
elif callMin>=31 and callMin <=60 :
    charge = (callMin - 30) * 1.5 + 60
elif callMin>=61 and callMin <=120 :
    charge = (callMin - 60) * 1 + 105
else :
    charge = (callMin - 120) * 0.5 + 165

print(str(charge) + " Rs")