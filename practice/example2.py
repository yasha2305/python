class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll)
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student(101, "Rahul", 88)

s1.display()