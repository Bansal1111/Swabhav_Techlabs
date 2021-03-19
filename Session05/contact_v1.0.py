import mysql.connector as mysql

try:
    con=mysql.connect(user='root',password='root',host='127.0.0.1',database='contact')
    print("Connected to "+str(con.is_connected()))

except Exception as ex:
    print(ex)

finally:
    if con.is_connected():
        data=con.cursor()
        user=0
        while(user!=5):
            print("Enter 1 for adding contact")
            print("Enter 2 for deleting contact")
            print("Enter 3 for editing contact")
            print("Enter 4 for displaying contact")
            print("Enter 5 for quiting")
            user=int(input("Enter your choice : "))
            if(user==1):
                fname=input("Enter first name : ")
                lname=input("Enter last name : ")
                mb=int(input("Enter mobile number : "))
                data.execute("INSERT INTO information(Firstname,Lastname,Mobile) VALUES(%s,%s,%s)",(fname,lname,mb))
                print("Contact saved successfully")
                print()
                con.commit()
            elif(user==2):
                data.execute("SELECT * FROM INFORMATION")
                ans=data.fetchall()
                for i in ans:
                    print(i)
                user_id=float(input("Enter which serial no. to be deleted : "))
                data.execute("DELETE FROM information where PersonID= '%d' " %(user_id))
                con.commit()
                print("Data delete successfully")
                print()
            elif(user==3):
                user_field=input("Enter which field need to be edited : ")
                user_old=input("Enter which field need to be edited : ")
                user_new=input("Enter the new one : ")
                data.execute("UPDATE information SET %s = %s WHERE %s=%s ",(user_field,user_new,user_field,))
                print("DATA Edited successfully")
            elif(user==4):
                data.execute("SELECT * FROM INFORMATION")
                ans=data.fetchall()
                for i in ans:
                    print(i)
                print()
            elif(user==5):
                break
            else:
                print("Enter correect value")
        con.close()
        data.close()
    print()
    print("conntection closed")
print("program ends here")
print()