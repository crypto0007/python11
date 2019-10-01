import mysql.connector;

con=mysql.connector.connect(host="localhost",database="Stdentpy",user="root",password="")

print(con)

CT="create table studentdetail ("
CT=CT+"name varchar(20),"
CT=CT+"birthdate date,"
CT=CT+"gender char(1),"
CT=CT+"semester int(1),"
CT=CT+"rollno int,"
CT=CT+"py_m decimal,"
CT=CT+"j_m decimal,"
CT=CT+"php_m decimal,"
CT=CT+"tot decimal,"
CT=CT+"per decimal,"
CT=CT+"grade char(1))"

cursor=con.cursor()
cursor.execute(CT)
