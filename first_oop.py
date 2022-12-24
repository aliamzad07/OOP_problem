class Student:
    roll = ""
    gpa = ""
    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll Number : {self.roll}, GPA value: {self.gpa}")


rahim = Student()
print(isinstance(rahim,Student))
rahim.set_value(7,3.50)
rahim.display()

karim = Student()
karim.set_value(8,3.71)
karim.display()