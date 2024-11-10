# Class contains objects.
# In a class you can define a function.
# In class it is better to define a init function which contains
# all the variable that are used in the object
# self is a blank object




# The following is the class

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades)/len(self.grades)
    
    def print_info(self):
        print(f"{self.name} have grades {self.grades}")
    
# The following is the object of the class

student_one = Student('Ahad', [70, 80, 90, 99])
student_two = Student('Ali', [90, 66, 78, 77])

#print(student_one.__class__) # This will just print the type of the class
#print(student_two.__class__) # This will just print the type of the class

#print(student_one.name)

print(student_one.average())
print(Student.average(student_one)) # This is another way to same thing as the first one

student_one.print_info()