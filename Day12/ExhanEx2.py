class sample:
    def m1(self):
        x,y=10,0
        try:
            z=x/y
        except ZeroDivisionError as e:
            print("Cannot Divisible by Zero")
            print("Division by0 not accepted")
        except Exception as e1:
            print(e1)
        else:
            print("Division",z)
        finally:
            print("Executing finally block")

        x=0
        y=0
    print("out of try,except,else,and finally block.")







