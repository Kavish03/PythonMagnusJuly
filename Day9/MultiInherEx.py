class Father:
    def home(self):
        print("2 Flats and 2 Plots with house")
class Mother:
    def car(self):
        print("2 cars")
    def cash(self):
        print("1 Billion cash")
class Son(Father,Mother):
    pass
obj1= Son()
obj1.home()
obj1.car()
obj1.cash()



