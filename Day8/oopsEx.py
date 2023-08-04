class Sample:
    a=10
    b=20
    def m1(self):
        print("M1 Function")

obj1 = Sample() #creating an object for class
obj2 = Sample()
print(obj1.a+obj2.b)# a+b
obj1.m1()
print(type(obj1))
