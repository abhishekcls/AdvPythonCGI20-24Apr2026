#Iterable
'''
list,set,tuple,dict,str,...
'''
l=[1,4,2]
# for ll in l:
#     print(ll)

#Iterator
try:
    it=iter(l)#Lazy
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))#Error: StopIteration
except StopIteration:
    print("Can't read further")

print("Done")