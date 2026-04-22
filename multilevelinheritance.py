# class GrandFather:
#     def money(self):
#         print("GrandFather's Money")

# class Father(GrandFather):
#     def money(self):
#         super().money()
#         print("Father's Money")

# class Child(Father):
#     def money(self):
#         super().money()
#         print("Child's Money")

# c=Child()
# c.money()

# print(Child.mro())#method resolution order


#Hybrid
class A:
    def disp(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()
d.disp()
print(D.mro())