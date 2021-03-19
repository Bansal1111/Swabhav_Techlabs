import mysql.connector as mysql
con = mysql.connect(user='root', password='root', host='127.0.0.1', database='contact')
def all_data():
    data = con.cursor()
    data.execute("SELECT * FROM INFORMATION")
    ans = data.fetchall()
    return ans
def check_user(name,contact):
    data = con.cursor()
    data.execute("SELECT * FROM INFORMATION WHERE FirstName ='%s' AND Mobile='%s' " % (name, contact))
    ans=data.fetchone()
    if(ans):
        return True
    else:
        return False
def add_contact(fname,lname,contact):
    data = con.cursor()
    print(fname,lname,contact)
    data.execute("INSERT INTO INFORMATION(Firstname,Lastname,Mobile) VALUES(%s,%s,%s)", (fname, lname, contact))
    con.commit()
