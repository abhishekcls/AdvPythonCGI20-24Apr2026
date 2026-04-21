'''
list [] -> mutable(change)
tuple () -> immutable(can't change)
set  {} -> unique, ordered
'''

l=[1,4,2,4,7]
l.append(11)
print(l)
print(type(l))

t=(1,4,2,4,7)
print(t)
print(type(t))

s={1,4,2,4,7}
print(s)
print(type(s))