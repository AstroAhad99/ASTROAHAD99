# Inheritance is used in python to extend the capability of a Python class
# The purpose of inheritance is to reduce the duplication of variables used in classes

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)
    

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5
    

rolf = WorkingStudent('Rolf', 'MIT', 15.5)
print(rolf.salary)

rolf.marks.append(57)
rolf.marks.append(96)
rolf.marks.append(88)

print(rolf.average())
print(rolf.weekly_salary())

# If we create an object with Student class and try to access the 
# Weekly salary function then it wil give an error because that function
# does not exist in the Student class

anna = Student('Anna', 'MIT')
#print(anna.weekly_salary())
# The above print will give an error
