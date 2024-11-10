# In the class if you have some methods that are just used to calculate
# some values then it is good option to use decorator (@) which makes
# the method not to use () closed brackets to call that method/function

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

    @property
    def weekly_salary(self):
        return self.salary * 37.5
    

rolf = WorkingStudent('Rolf', 'MIT', 15.5)
print(rolf.salary)

#print(rolf.weekly_salary())
print(rolf.weekly_salary)

