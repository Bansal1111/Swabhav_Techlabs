from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='root', database='iimft')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

def update_country(country_name,country_id):
    con, cursor = conn()
    query='UPDATE country  SET country_name="{}" WHERE country_id = {}'.format(country_name,country_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def update_state(state_id,state_name,country_name):
    con, cursor = conn()
    cursor.execute('SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name))
    country_id =cursor.fetchall()
    query='UPDATE state  SET state_name="{}",country_id={} WHERE state_id = {}'.format(state_name,country_id[0][0],state_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def update_venue(venue_id,venue_city,venue_addr,state_name,country_name):
    con, cursor = conn()
    cursor.execute('SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name))
    state_id =cursor.fetchall()
    cursor.execute('SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name))
    country_id =cursor.fetchall()
    query='UPDATE venue  SET venue_city="{}",venue_addr="{}",state_id={},country_id={} WHERE venue_id = {}'.format(venue_city,venue_addr,state_id[0][0],country_id[0][0],venue_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def update_stall(stall_id,stall_no,stall_price,stall_size,is_booked,event_name):
    con, cursor = conn()
    cursor.execute('SELECT event_id  FROM eventt WHERE event_name = "{}"'.format(event_name))
    event_id =cursor.fetchall()
    query='UPDATE stall  SET stall_no={},stall_price={},stall_size={},is_booked="{}",event_id={} WHERE stall_id = {}'.format(stall_no,stall_price,stall_size,is_booked,event_id[0][0],stall_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def update_industry(industry_name,industry_id):
    con, cursor = conn()
    query='UPDATE industry  SET industry_name="{}" WHERE industry_id = {}'.format(industry_name,industry_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def update_exhibitor(exhibitor_id,exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_name,state_name,country_name):
    con, cursor = conn()
    cursor.execute('SELECT industry_id  FROM industry WHERE industry_name = "{}"'.format(industry_name))
    industry_id =cursor.fetchall()
    cursor.execute('SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name))
    state_id =cursor.fetchall()
    cursor.execute('SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name))
    country_id =cursor.fetchall()
    query='UPDATE exhibitor SET exhibitor_name="{}",email_id="{}",phone_no="{}",company_name="{}",company_description="{}",company_addr="{}",company_pin_code={},industry_id={},state_id={},country_id={} WHERE exhibitor_id = {}'.format(exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_id[0][0],state_id[0][0],country_id[0][0],exhibitor_id)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()