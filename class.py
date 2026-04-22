# class Person:
#     def __init__(self):
#         print("constructor")
#     def disp(self):
#         print("Hello")

# p=Person()
# p.disp()

class Employee:
    company="ABC company"#static
    def __init__(self,eid,name,sal=10000):
        print("constructor")
        self.eid=eid #public
        self.name=name
        self.__sal=sal #private
    def __str__(self):
        return f"Name: {self.name}, eid: {self.eid} and sal: {self.__sal}"
    def disp(self):
        print(f"Hello {self.name}, your eid: {self.eid} and your sal: {self.__sal} you work in {self.company}")
    @staticmethod
    def show():
        print("Static Method")

Employee.show()
print(Employee.company)
e=Employee(101,"Gaurav",15000)
e.disp()
print(e)
print(type(e))

e2=Employee(102,"Ravi")
e2.disp()
print(e2.name)
#print(e2.__sal)#not accessible