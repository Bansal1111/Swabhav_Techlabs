import mysql.connector as mysql

try:
    con=mysql.connect(user='root',password='root',host='127.0.0.1',database='world')
    print("connected to"+str(con.is_connected()))
    code=input("Enter country code :")
    query= "SELECT * FROM COUNTRY WHERE CODE='" + code + "'"
    print(query)
    cursor=con.cursor()
    cursor.execute(query)
    record=cursor.fetchall()

    for row in record:
        print(row[0],row[1])

except Exception as ex:
    print(ex)

finally:
    if con.is_connected():
        con.close()
        cursor.close()
    print("conntection closed")
print("program ends here")