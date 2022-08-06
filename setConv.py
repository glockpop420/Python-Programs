a=5
b=10
c=[1,2,3,4,5,6,7]
d=(27,29,31,33)
"""conversion of list into tuple and vice versa"""
e=tuple(c)
f=list(d)
print(type(e))
print(type(f))
"""gives the index"""
Ae=enumerate(c)
print(Ae)
"""gives the list of the index number of each element of the array"""
g=list(Ae)
print(g)
c.append(8)
print(c)

