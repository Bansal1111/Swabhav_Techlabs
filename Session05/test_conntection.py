import mysql.connector as mysql

try:
    con=mysql.connect(user='root',password='root',host='127.0.0.1',database='world')
    print("connected to"+str(con.is_connected()))

except Exception as ex:
    print(ex)

finally:
    if con.is_connected():
        con.close()
    print("conntection closed")
print("program ends here")