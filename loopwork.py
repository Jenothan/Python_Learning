
'''
x=1
while x<=9 :
    print(x, end='')
    x+=2
 '''                       # answer =>        #1 3 5 7 9 

'''
x=2
while x<=10 :
    print(x, end='')
    x+=2
    '''                 # answer =>        #2 4 6 8


'''
x=1
y=1
while x<=15 :
    print(x, end='')
    y=y+1
    x=x+y
'''                     # answer =>        #1 3 6 10 15 
    
'''   
x=1
y=1
while x<=25 :
    print(x, end='')
    y=y+2
    x=x+y
'''                     # answer =>        #1 4 9 16 25    
    
 

'''
x=1
while x<=5 :
    if x%2==0 :
        print("*", end='')
    else :
        print(x, end='')
    x+=1 

'''                         # answer =>        #1 * 3 * 5 


'''
x=1
while x<=5 :
    if x%2==0 : 
        print(x, "**")
    else :
        print(x, "*")
    x+=1
'''                             # answer =>         #1 *
                                                    #2 * *
                                                    #3 *
                                                    #4 * *
                                                    #5 *


'''
x=1
while x<=5 :
    y=1
    while y<=5 :
        print(y, end='')
        y+=1
    print()
    x+=1
'''                             # answer =>         #1 2 3 4 5
                                                    #1 2 3 4 5
                                                    #1 2 3 4 5
                                                    #1 2 3 4 5
                                                    #1 2 3 4 5
                                                    

'''
x=5
while x>=1 : 
    y=5
    while y>=1 :
        print(y, end='')
        y-=1
    print()
    x-=1
'''                             
                               # answer =>          #5 4 3 2 1
                                                    #5 4 3 2 1
                                                    #5 4 3 2 1
                                                    #5 4 3 2 1
                                                    #5 4 3 2 1 

'''
x=1
while x<=5 :
    y=1
    while y<=5 :
        print(x, end='')
        y+=1
    print()
    x+=1
'''                 
                                    # answer =>     #1 1 1 1 1
                                                    #2 2 2 2 2
                                                    #3 3 3 3 3
                                                    #4 4 4 4 4
                                                    #5 5 5 5 5 

'''
y=1
while y<=5 :
    x=1
    while x<=5 :
        if x%2==0 :
            print("*", end='')
        else :
            print(x, end='')
        x+=1 
    print()
    y+=1
'''
                                # answer =>         #1 * 3 * 5 
                                                    #1 * 3 * 5 
                                                    #1 * 3 * 5 
                                                    #1 * 3 * 5 
                                                    #1 * 3 * 5 


'''
x=1
while x<=5 :
    y=1
    while y<=x :
        print(y, end='')
        y+=1
    print()
    x+=1
''' 
                                # answer =>         #1 
                                                    #1 2 
                                                    #1 2 3 
                                                    #1 2 3 4 
                                                    #1 2 3 4 5