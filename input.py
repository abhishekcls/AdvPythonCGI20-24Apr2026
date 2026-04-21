name=input("Enter your name: ")
print(name)

age=input("Enter Age: ")

if age.isdigit():
    age=int(age)
    print(age,type(age))
    print(age+10)
else:
    print("Enter numbers only")