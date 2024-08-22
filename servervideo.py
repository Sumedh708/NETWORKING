import random
import time as t
import mysql.connector
import socket
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database="videoapp")
c=mydb.cursor()
#Defining
    
global name
global age
global gen
global hcm
global weight

#establish connection
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
port = 1255
s.bind((host,port))
s.listen(5)
print("Signals sent...Waiting")
#Asking details
def main():
    try:
        while True:
            conn,addr=s.accept()
            print("came")
            mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database="videoapp")
            c=mydb.cursor()
            ipaddr=conn.recv(1024).decode()
            sql=f"SELECT name FROM BMI WHERE ipaddr='{ipaddr}'"
            c.execute(sql)
            result=c.fetchall()
            for i in result:
                print(i[0])
            if result==[]:
                    conn.send(bytes("new",'utf-8'))
                    name=conn.recv(1024).decode()
                    age=conn.recv(1024).decode()
                    age=int(age)
                    gen=conn.recv(1024).decode()
                    hcm=conn.recv(1024).decode()
                    hcm=int(hcm)
                    weight=conn.recv(1024).decode()      
                    sql = f"INSERT INTO BMI(ipaddr,name,gender,age,height,weight) VALUES ('{ipaddr}','{name}','{gen}',{age},{hcm},{weight})"
                    c.execute(sql)
                    mydb.commit()
                    print("done")
            else:
                    conn.send(bytes("continue",'utf-8'))
                    sql1=f"Select * from BMI where ipaddr='{ipaddr}' "
                    c.execute(sql1)
                    r=c.fetchall()
                    x=tuple(r)
                    print(x)
                    for i in x:
                        ip,name,age,gen,hcm,weight=i
                    t.sleep(1)
                    conn.send(bytes(ip,'utf-8'))
                    t.sleep(1)
                    conn.send(bytes(name,'utf-8'))
                    print(name,'done')
                    t.sleep(1)
                    conn.send(bytes(str(gen),'utf-8'))
                    t.sleep(1)
                    conn.send(bytes(str(age),'utf-8'))
                    t.sleep(1)
                    conn.send(bytes(str(hcm),'utf-8'))
                    t.sleep(1)
                    conn.send(bytes(str(weight),'utf-8'))
    except ConnectionResetError:
        print("1 exit")
        main()
                
main()

