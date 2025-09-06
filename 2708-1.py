'''
number = [33, 44, 56, 33, 56, 76]
print(number)
newnum = set(number)
print(newnum)
'''
a = {3, 5, 7, 8, 10}
b = {3, 5, 6, 8, 12}
#c=a|b
c= a.union(b)
#d=a&b
d=a.intersection(b)
e=a-b
f=b-a
#g=a^b
g=a.symmetric_difference(b)
print(c)
print(d)
print(e)
print(f)
print(g)