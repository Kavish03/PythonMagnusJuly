from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='0310',database='pythonmagnus')

c1=myDbConnection.cursor()

c1.execute("select * from indus")

result = c1.fetchall()

for i in result:
    print(i)


myDbConnection.close()
