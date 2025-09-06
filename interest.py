def calcInterest(amount, months):
    interest=0
    if months<3 or amount<0:
        print("Please enter valid amount or months")
    elif months==3:
        interest=12
    elif months==6:
        interest=12.5
    elif months==12:
        interest=13
    elif months==36:
        interest=14
    elif months==60:
        interest=15
    elif months>60:
        interest=15.5
    else:
        print("Invalid number....!")
        

    total=amount+amount*interest
    print(f"Total : {total}")
    
calcInterest(100000, 36)