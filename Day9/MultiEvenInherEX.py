class Grandparent:
    def a1(self):
        print("2 Assets")
class Parent(Grandparent):# a1 and a2
    def a2(self):
        print("3 Assets")
class Son(Parent):# a1, a2 and a3
        def a3(self):
            print("3 Assets")
obj1= Son()
obj2= Parent()
obj1.a1()
obj1.a2()
obj1.a3()

