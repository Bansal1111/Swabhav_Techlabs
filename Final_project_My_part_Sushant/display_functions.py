from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='root', database='iimft')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

def display_country():
    con,cursor = conn()
    cursor.execute('SELECT * FROM country')
    country = cursor.fetchall()
    close()
    return country

def display_state():
    con,cursor = conn()
    cursor.execute('SELECT state_id,state_name,country_name FROM state JOIN country ON state.country_id=country.country_id')
    state = cursor.fetchall()
    close()
    return state

def display_venue():
    con,cursor = conn()
    cursor.execute('SELECT venue_id,venue_city,venue_addr,state_name,country_name FROM venue JOIN state ON venue.state_id=state.state_id JOIN country ON venue.country_id=country.country_id ')
    venue = cursor.fetchall()
    close()
    return venue

def display_event():
    con,cursor = conn()
    cursor.execute('SELECT * FROM eventt')
    event = cursor.fetchall()
    close()
    return event

def display_stall():
    con,cursor = conn()
    cursor.execute('SELECT stall_id,stall_no,stall_price,stall_size,is_booked,event_name FROM stall JOIN eventt ON stall.event_id=eventt.event_id')
    stall = cursor.fetchall()
    close()
    return stall

def display_industry():
    con,cursor = conn()
    cursor.execute('SELECT * FROM industry')
    industry = cursor.fetchall()
    close()
    return industry

def display_exhibitor():
    con,cursor = conn()
    cursor.execute('SELECT exhibitor_id,exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_name,state_name,country_name FROM exhibitor JOIN industry ON exhibitor.industry_id=industry.industry_id JOIN state ON exhibitor.state_id=state.state_id JOIN country ON exhibitor.country_id=country.country_id ')
    exhibitor = cursor.fetchall()
    close()
    return exhibitor