class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade > 50:
            return True

    def __str__(self):
        return f"Student: {self.name}, Grade: {self.grade}"


Stud1 = Student("Ravi", 78)
Stud2 = Student("Beni", 38)

print(Stud1)
print(is_passing(Stud1))
