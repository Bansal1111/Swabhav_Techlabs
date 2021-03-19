import mysql.connector as mysql
con = mysql.connect(user='root', password='root', host='127.0.0.1', database='contact')
def all_data():
    data = con.cursor()
    data.execute("SELECT * FROM INFORMATION")
    ans = data.fetchall()
    return ans