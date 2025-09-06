a= {1,2,3}
b={1,2,3,4,5}
c = {4,5,6}

d = a|b|c
print(d)

e=a&b&c
print(e)

print(a<=b) #print(a.issubset(b))

print(b.issubset(a))
print(b>=a)