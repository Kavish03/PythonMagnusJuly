from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='0310',database='pythonmagnus')

c1=myDbConnection.cursor()
vcname = input("Enter the cname value:")
vcnum = int(input("Enter the cnum value:"))
vsal = int(input("Enter the sal Value:"))
vlocation = input("Enter the location value:")


c1.execute("Insert into indus(cname,cnum,sal,location) values(%s,%s,%s,%s)",(vcname,vcnum,vsal,vlocation))

myDbConnection.commit()
myDbConnection.close()

