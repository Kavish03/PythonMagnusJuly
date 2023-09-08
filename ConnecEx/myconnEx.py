from mysql import connector
myDbconnection = connector.connect(host='localhost',user='root',password='0310',database='pythonmagnus')

c1 = myDbconnection.cursor()
#cursor is a pointer which locates in a processing area/temporary memory area
#c1.execute("drop table if exists Indus")
#c1.execute("create table Indus(cname varchar(20),cnum int,sal int,location varchar(15))")
#c1.execute("Insert into Indus values('Kevin',6123,26000,'Texas')")
#c1.execute("Insert into Indus values('Max',9020,27000,'Florida')")
sql = "insert into indus Values(%s,%s,%s,%s)"
data = ('Martin',4240,30000,'DC')
c1.execute(sql,data)
myDbconnection.commit()
myDbconnection.close()



