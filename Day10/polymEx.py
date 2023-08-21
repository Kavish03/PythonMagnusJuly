class India():
     def Capital(self):
         print("Delhi is the capital of Tamilnadu")

     def Language(self):
         print("Hindi is the official Language")

     def type(self):
         print("India is a developing State")

class USA():
    def Capital(self):
        print("Washington is the Capital of USA")

    def Language(self):
        print("English is official Language")

    def type(self):
        print("USA is a developed Country")

obj_India =India()
obj_USA =USA()

for Country in ( obj_India,obj_USA):
    Country.Capital()
    Country.Language()
    Country.type()




