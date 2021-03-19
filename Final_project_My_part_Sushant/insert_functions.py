from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='root', database='iimft')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

def insert_country(country_name):
    con, cursor = conn()
    query = f"INSERT INTO `country` (`country_name`) VALUES ('{country_name}');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_state(state_name,country_name):
    con, cursor = conn()
    cursor.execute('SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name))
    country_id =cursor.fetchall()
    query = f"INSERT INTO `state` (`state_name`,`country_id`) VALUES ('{state_name}',{country_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_venue(venue_city,venue_addr,state_name,country_name):
    con, cursor = conn()
    cursor.execute('SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name))
    state_id =cursor.fetchall()
    cursor.execute('SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name))
    country_id =cursor.fetchall()
    query = f"INSERT INTO `venue` (`venue_city`,`venue_addr`,`state_id`,`country_id`) VALUES ('{venue_city}','{venue_addr}',{state_id[0][0]},{country_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_stall(stall_no,stall_price,stall_size,is_booked,event_name):
    con, cursor = conn()
    cursor.execute('SELECT event_id  FROM eventt WHERE event_name = "{}"'.format(event_name))
    event_id =cursor.fetchall()
    query = f"INSERT INTO `stall` (`stall_no`,`stall_price`,`stall_size`,`is_booked`,`event_id`) VALUES ({stall_no},{stall_price},{stall_size},'{is_booked}',{event_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_industry(industry_name):
    con, cursor = conn()
    query = f"INSERT INTO `industry` (`industry_name`) VALUES ('{industry_name}');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_exhibitor(exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_name,state_name,country_name):
    con, cursor = conn()
    cursor.execute('SELECT industry_id  FROM industry WHERE industry_name = "{}"'.format(industry_name))
    industry_id =cursor.fetchall()
    cursor.execute('SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name))
    state_id =cursor.fetchall()
    cursor.execute('SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name))
    country_id =cursor.fetchall()
    query = f"INSERT INTO `exhibitor` (`exhibitor_name`,`email_id`,`phone_no`,`company_name`,`company_description`,`company_addr`,`company_pin_code`,`industry_id`,`state_id`,`country_id`) VALUES ('{exhibitor_name}','{email_id}','{phone_no}','{company_name}','{company_description}','{company_addr}',{company_pin_code},{industry_id[0][0]},{state_id[0][0]},{country_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()