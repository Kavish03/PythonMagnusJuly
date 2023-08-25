class sample:
    def m1(self):
        a=5
        b='0'
        try:
            print(a/b)
        except TypeError as e:
            print('unsupported operation')
        except ZeroDivisionError as e1:
            print('Division by Zero not allowed')
        except Exception as e2:
             print(e2)
obj1=sample()
obj1.m1()
print("End of the program")






