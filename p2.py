import mysql.connector;
#from mysql.connector import Error;

class exractdetail:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",database="Stdentpy",user="root",password="")
        self.cursor=con.cursor()
        
    def get(self):
        self.name=input("Enter Name")
        self.birthdate=input("Enter bithdate")
        self.gender=input("Enter gender")
        self.semester=input("Enter rollno")
        self.py_m=input("Enter python Marks")
        self.j_m=input("Enter java marks")
        self.php_m=input("Enter php marks")

    def insert(self):
        self.IITT="insert into studendetail (name, birthdate,gender,semseter,rollno,py_m,j_m,php_m) values ("+self.name+",'"+self.birthdate+"','"f.semester"','"self.rollno"','"self.py_m"','"self.j_m"','"self.php_m"')"
        self.cursor(self.IITT)
        self.con.commit()
        
    '''def caltot(self):
        self.tot=self.py_m+self.j_m+self.php_m;

    def calper(self):
        self.per=(self.tot/300)*100

    def calgrd(self):'''
        


#print(con)
s1=exractdratil();
while(1):
    print("1.Get Data:")
    print("2.Insert")
    c=int(input("Choice"))
    
    if(c==1):
        s1.get();
    elif(c==2):
        s1.insert();
