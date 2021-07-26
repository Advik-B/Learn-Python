# print (">-Name-<")
# name = input("--->")
# print (">-Age-<")
# age = int(input('--->'))
# print ('>-Marks-<')
# marks = int(input('--->'))

class Student:
    def __init__(self,name,age,marks=0):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f'Hi {self.name}')
        print(f'Your age is {self.age}')
        print(f'Your marks is {self.marks}')
s1 = Student("Advik",22,95)  
s1.display()