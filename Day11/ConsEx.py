class Family:
    members=10
    def __init__(self,count):
        self.member=count
    def display(self):
        print("Number of Family members",self.member)

obj_family = Family(20)
obj_family.display()



