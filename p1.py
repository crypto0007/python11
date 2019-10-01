import mysql.connector
from mysql.connector import Error;



class Student_Class:
    
    
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",user="root",password="",port="3308",database="py_student");
        self.mycursor=self.con.cursor();

    def getData(self):
        self.r_no=input("ENTER ROLL NUMBER:");
        self.name=input("ENTER NAME:");
        self.b_date=input("ENTER BIRTH DATE:");
        self.gen=input("ENTER GENDER [F/M]:");
        self.sem=input("ENTER SEM:");
        self.py_marks=input("ENTE PYTHON MARKS:");
        self.j_marks=input("ENTE JAVA MARKS:");
        self.php_marks=input("ENTE PHP MARKS:");
        
    def insertData(self):
         
         self.insertQuery="INSERT INTO student_table(roll_no, name, b_date, gender, sem, python_mraks, java_mraks, php_mraks) VALUES ("+self.r_no+",'"+self.name+"','"+self.b_date+"','"+self.gen+"',"+self.sem+","+self.py_marks+","+self.j_marks+","+self.php_marks+")";
         
       
         data=self.mycursor.execute(self.insertQuery);
         self.con.commit();
    def cal_total(self):
        self.updateTotal="UPDATE student_table set total_mraks=python_mraks+java_mraks+php_mraks";
        self.mycursor.execute(self.updateTotal);
        self.con.commit();
         
    def cal_per(self):
        self.updatePer="UPDATE student_table set percentage=total_mraks*100/300";
        self.mycursor.execute(self.updatePer);
        self.con.commit();
        
    
        


s1=Student_Class();
while(1):
    
    print("1.getdata");
    print("2.INSERT DATA");
    print("3.CALCULATE  TOTAL");
    print("4.CALCULATE  PERCENTAGE");
    ch=int(input("ENTER YOUR CHOICE"));

    if(ch==1):
        s1.getData();
    elif(ch==2):
        s1.insertData();
    elif(ch==3):
        s1.cal_total();
    elif(ch==4):
        s1.cal_per();        
    else:
        print("ERROR");
    


        
        
        
        
