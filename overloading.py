# def add(a,b,c=0):
#     print(a+b+c)

# add(2,3)
# add(2,3,4)

# def sum(*args):
#     total=0
#     for a in args:
#         total+=a
#     print(total)

# sum(1)
# sum(2,3)
# sum(3,5,6,7,8,9,0,8)

# def show(a):
#     print(a)

# show(100)
# show(5.7)
# show("Abhishek")

##############################################
from functools import singledispatch

@singledispatch
def process_data(data):
    print("Unsupported data type")

@process_data.register(int)
def _(data):
    print(f"Processing int: {data*2}")

@process_data.register(list)
def _(data):
    print(f"Processing list: {len(data)}")

process_data(10)
process_data([1,2,3,4,5])
process_data(4.5)