class Father:
    def money(self):
        print("Father's Money")

class Mother:
    def money(self):
        print("Mother's Money")

class Child(Father,Mother):
    def money(self):
        super().money()
        Mother().money()
        print("Child's Money")

c=Child()
c.money()

print(Child.mro())#method resolution order