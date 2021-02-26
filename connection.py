from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='abc123', database='pyintern')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

def new_disp_visitor():
    con,cursor = conn()
    cursor.execute('SELECT * FROM visitor')
    visitor = cursor.fetchall()
    close()
    return visitor
