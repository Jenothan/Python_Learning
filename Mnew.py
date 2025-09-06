#s = 'Welcome to python'
'''print(s)
print(len(s))
print(s[0])
print(s[-17])'''

#i=-abs(len(s))
'''
while i<len(s) :
    print(s[i], end='')
    i+=1
    '''
'''
while i<=(-1) :
    print(s[i], end='')
    i+=1
'''
'''
for i in s :ge
    print(i, end='')
 '''   
    
'''
for i in range(len(s)-1, -1, -1) :
    print(s[i], end='')
'''
'''
for i in reversed(s) :
    print(i, end='')'''
    
'''
a=s[0:1]
print(a)


'''




s = input ("Enter your date of birth... eg: DD/MM/YYYY.....:  ")
print(s)

date=s[0:2]
month=s[3:5]
year=s[6:10]
total1=0
total=0


total = int(date)+int(month)+int(year)
if total%9!=0 :
    total1=total%9
else :
    total1=9
print(f"Your Numorology number:  {total1}")


'''
if int(date)%9 != 0 :
    date1=int(date)%9
else :
    date1=9
print(date1)

if int(month)%9 != 0 :
    month1=int(month)%9
else :
    month1=9
print(month1)

if int(year)%9 != 0 :
    year1=int(year)%9
else :
    year1=9
print(year1)'''

'''
print(total)

if int(total)%9!=0 :
    total1=int(total)%9
else :
    total1=9
print(total1)'''
'''
for i in date :
    if len(date)-1 > 0 :
        date1+=int(i)
    for i in month :
        if len(month)-1 > 0 :
            month1 += int(i)
        for i in year :
            if len(year)-1 > 0 :
                year1 += int(i)
                
print(date1, month1, year1)
    
#print(total)'''

'''
number=0
total = int(date) + int (month) + int(year)
total = str(total)
for i in total :
    number+=int(i)
print(number)'''