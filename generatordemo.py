def generate(n):
    for i in range(n):
        yield i#generator

res=generate(5)
print(res)
print(type(res))

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
#print(next(res))#Error