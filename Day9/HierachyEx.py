class Teacher:
    def english(self):
        print("English Language")
class Student1(Teacher):
    def maths(self):
        print("Maths subject")
class Student2(Teacher):
    pass
obj1= Student1()
obj2= Student2()
obj1.english()
obj1.maths()
obj2.english()
obj2.maths()


