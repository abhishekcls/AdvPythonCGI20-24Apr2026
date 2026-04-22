# class Shape:
#     def area(self):
#         print("Shape's area")

# class Circle(Shape): #inheritance
#     def area(self):
#         print("Circle's area")

# c=Circle()
# c.area()

class Parent:
    def __init__(self,a):
        print("Parent cons")
        self.a=a
    def money(self):
        print("Parent's Money")

class Child(Parent):
    def __init__(self,a,b):
        super().__init__(a)
        print("Child cons")
        self.b=b

    def __str__(self):
        return f"A: {self.a} B: {self.b}"

c=Child(10,20)
c.money()
print(c)
