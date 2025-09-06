x=[
    [10, 20, 30],
    [70, 90, 25],
    [40, 98, 26],
    ]

i=0
while i<len(x):
    j=0
    while j<len(x[i]):
        print(x[i][j], end='')
        j+=1
    print()
    i+=1
    
    
'''
5 students 3 subjects
output: 
| Students | Tamil | Maths | Science | Total | Average | Results |
'''

