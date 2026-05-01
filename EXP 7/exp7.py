print("--- OOP DEMONSTRATION ---")

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

    def update_marks(self, new_marks):
        self.marks = new_marks

student1 = Student("Alice", 20, 85)

print("Initial Student Details:")
student1.display()

student1.update_marks(90)

print("After Updating Marks:")
student1.display()


class GraduateStudent(Student):
    def __init__(self, name, age, marks, degree):
        super().__init__(name, age, marks)
        self.degree = degree

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}, Degree: {self.degree}")


grad_student = GraduateStudent("Bob", 24, 88, "MSc")

print("Graduate Student Details:")
grad_student.display()S
