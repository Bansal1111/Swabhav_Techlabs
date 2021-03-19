from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='root', database='iimft')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

def delete_country(countryid):
    con, cursor = conn()
    query='DELETE FROM country WHERE country_id = {} '.format(countryid)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete_state(state_id):
    con, cursor = conn()
    query='DELETE FROM state WHERE state_id = {} '.format(state_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete_venue(venue_id):
    con, cursor = conn()
    query='DELETE FROM venue WHERE venue_id = {} '.format(venue_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete_stall(stall_id):
    con, cursor = conn()
    query='DELETE FROM stall WHERE stall_id = {} '.format(stall_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete_industry(industry_id):
    con, cursor = conn()
    query='DELETE FROM industry WHERE industry_id = {} '.format(industry_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete_exhibitor(exhibitor_id):
    con, cursor = conn()
    query='DELETE FROM exhibitor WHERE exhibitor_id = {} '.format(exhibitor_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()