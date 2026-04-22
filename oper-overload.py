class Subject:
    def __init__(self,m):
        self.marks=m

    def __add__(self, other):
        t=Subject(0)
        t.marks=self.marks+other.marks
        return t
    
    def __str__(self):
        return f"Marks: {self.marks}"

eng=Subject(75)
math=Subject(99)

total=eng+math
print(total)