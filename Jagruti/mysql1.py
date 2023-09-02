from .connection import MySQLConnection
my=mysql.connector.connect(host="localhost",user="root",password="",database="school")
s=myconn.cursor()
try:
    s.excute("select * from stud")
    result=s.fetchall()
    for i in result:
        print(i)
except:
    myconn.rollback()

