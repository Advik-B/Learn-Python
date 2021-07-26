class Student:
    def __init__(self):
        self.name = "Advik"
        self.age = 14
        self.marks = 100
        self.percentage = 100
    def talk(self):
        print ("Name:-",self.name)
        print ("Age:-",self.age)
        print ("Marks:-",self.marks)
        print ("Percentage:-",self.percentage)



s1 = Student()  
s1.talk()
s1.name = "Ziya"
s1.talk()