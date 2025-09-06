marks = input("Enter your mark : ")
marks=int(marks)

#My own work
'''
if marks>=80 :
    print("You got A pass")
elif marks>=60 :
    print("You got B pass")
elif marks>=50 :
    print("You got c pass")
elif marks>=35 :
    print("You got s pass")
else :
    print("you are failed")
    '''
#question basic answer

'''
if marks>=80 :
    print("A")
else :
    if marks>=65 :
        print("B")
    else :
        if marks>=55 :
            print("C")
        else :
            if marks>=45 :
                print("S")
            else :
                print("F")   
'''


#question advanced answer

if marks>=0 and marks<=100 :
    if marks >= 75 and marks<=100 :
        print("A")
    elif marks >= 65 and marks<75:
        print("B")
    elif marks >= 55 and marks<65:
        print("C")
    elif marks >= 45 and marks<55:
        print("S")
    else :
        print("F")
else :
    print("Error: Invalid Marks")
