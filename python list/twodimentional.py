students = [
    ["Jenothan", 75, 80, 90],
    ["Sarangan", 80, 78, 80],
    ["Luxshan", 72, 85, 66],
    ["Praveenan", 55, 40, 99],
    ["Arthikan", 81, 80, 30],
]
print("-"*117)
print(f"|{'Student Name':<20}|{'Tamil':>15}|{'English':>15}|{'Physics':>15}|{'Total':>15}|{'Average':>15}|{'Results':>15}|")
print("-"*117)

i=0
while i<len(students):
    total=0
    average=0
    results=0
    total=students[i][1]+students[i][2]+students[i][3]
    average=total/3
    if average>100 or average<0 :
        print("Invalid Marks")
        break
    elif average>=75 :
        results='A'
    elif average>=65 :
        results='B'
    elif average>=55 :
        results='C'
    elif average>=35 :
        results='S'
    else :
        results='F'
    print(f"|{students[i][0]:<20}|{students[i][1]:>15}|{students[i][2]:>15}|{students[i][3]:>15}|{total:>15}|{average:02d:>15}|{results:>15}|")
    i+=1