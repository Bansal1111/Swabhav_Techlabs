from flask import Flask, render_template ,request,redirect
import display_functions , insert_functions , delete_functions , update_functions

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/country",methods=['GET','POST'])
def country():
    if(request.method=='POST'):
        insert_functions.insert_country(request.form['country_name'])
    country_data=display_functions.display_country()
    return render_template("country.html",country_data=country_data)

@app.route("/delete/<int:country_id>")
def delete(country_id):
    delete_functions.delete_country(country_id)
    return redirect("/country")

@app.route("/update/<int:country_id>/<string:country_name>",methods=['GET','POST'])
def update(country_id,country_name):
    if(request.method=='POST'):
        update_functions.update_country(request.form['country_name'],country_id)
        return redirect("/country")
    return render_template("update_country.html",country_id=country_id,country_name=country_name)






#-------------------State----------------------
@app.route("/state",methods=['GET','POST'])
def state():
    if(request.method=='POST'):
        insert_functions.insert_state(request.form['state_name'],request.form['country_name'])
    state_data=display_functions.display_state()
    country_data=display_functions.display_country()
    return render_template("state.html",state_data=state_data,country_data=country_data)

@app.route("/delete_state/<int:state_id>")
def delete_state(state_id):
    delete_functions.delete_state(state_id)
    return redirect("/state")

@app.route("/update/<int:state_id>/<string:state_name>/<string:country_name>",methods=['GET','POST'])
def update_state(state_id,state_name,country_name):
    if(request.method=='POST'):
        update_functions.update_state(state_id,request.form['state_name'],request.form['country_name'])
        return redirect("/state")
    country_data = display_functions.display_country()
    return render_template("update_state.html",state_id=state_id,state_name=state_name,country_name=country_name,country_data =country_data)





#-------------------Venue----------------------
@app.route("/venue",methods=['GET','POST'])
def venue():
    if(request.method=='POST'):
        insert_functions.insert_venue(request.form['venue_city'],request.form['venue_addr'],request.form['state_name'],request.form['country_name'])
    venue_data=display_functions.display_venue()
    state_data=display_functions.display_state()
    country_data=display_functions.display_country()
    return render_template("venue.html",venue_data=venue_data,state_data=state_data,country_data=country_data)

@app.route("/delete_venue/<int:venue_id>")
def delete_venue(venue_id):
    delete_functions.delete_venue(venue_id)
    return redirect("/venue")

@app.route("/update_venue/<int:venue_id>/<string:venue_city>/<string:venue_addr>/<string:state_name>/<string:country_name>",methods=['GET','POST'])
def update_venue(venue_id,venue_city,venue_addr,state_name,country_name):
    if(request.method=='POST'):
        update_functions.update_venue(venue_id,request.form['venue_city'],request.form['venue_addr'],request.form['state_name'],request.form['country_name'])
        return redirect("/venue")
    state_data=display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template("update_venue.html",state_data=state_data,country_data=country_data,venue_id=venue_id,venue_city=venue_city,venue_addr=venue_addr,state_name=state_name,country_name=country_name)






#-------------------Stall----------------------
@app.route("/stall",methods=['GET','POST'])
def stall():
    if(request.method=='POST'):
        insert_functions.insert_stall(request.form['stall_no'],request.form['stall_price'],request.form['stall_size'],request.form['is_booked'],request.form['event_name'])
    stall_data = display_functions.display_stall()
    event_data = display_functions.display_event()
    return render_template("stall.html",stall_data=stall_data,event_data=event_data)

@app.route("/delete_stall/<int:stall_id>")
def delete_stall(stall_id):
    delete_functions.delete_stall(stall_id)
    return redirect("/stall")

@app.route("/update_stall/<int:stall_id>/<int:stall_no>/<float:stall_price>/<float:stall_size>/<string:is_booked>/<string:event_name>",methods=['GET','POST'])
def update_stall(stall_id,stall_no,stall_price,stall_size,is_booked,event_name):
    if(request.method=='POST'):
        update_functions.update_stall(stall_id,request.form['stall_no'],request.form['stall_price'],request.form['stall_size'],request.form['is_booked'],request.form['event_name'])
        return redirect("/stall")
    event_data = display_functions.display_event()
    return render_template("update_stall.html",event_data=event_data,stall_id=stall_id,stall_no=stall_no,stall_price=stall_price,stall_size=stall_size,is_booked=is_booked,event_name=event_name)







#----------------------------Industry--------------------------------
@app.route("/industry",methods=['GET','POST'])
def industry():
    if(request.method=='POST'):
        insert_functions.insert_industry(request.form['industry_name'])
    industry_data=display_functions.display_industry()
    return render_template("industry.html",industry_data=industry_data)

@app.route("/delete_industry/<int:industry_id>")
def delete_industry(industry_id):
    delete_functions.delete_industry(industry_id)
    return redirect("/industry")


@app.route("/update_industry/<int:industry_id>/<string:industry_name>",methods=['GET','POST'])
def update_industry(industry_id,industry_name):
    if(request.method=='POST'):
        update_functions.update_industry(request.form['industry_name'],industry_id)
        return redirect("/industry")
    return render_template("update_industry.html",industry_id=industry_id,industry_name=industry_name)


#-------------------Exhibitor----------------------
@app.route("/exhibitor",methods=['GET','POST'])
def exhibitor():
    if(request.method=='POST'):
        insert_functions.insert_exhibitor(request.form['exhibitor_name'],request.form['email_id'],request.form['phone_no'],request.form['company_name'],request.form['company_description'],request.form['company_addr'],request.form['company_pin_code'],request.form['industry_name'],request.form['state_name'],request.form['country_name'])
    exhibitor_data = display_functions.display_exhibitor()
    industry_data=display_functions.display_industry()
    state_data=display_functions.display_state()
    country_data=display_functions.display_country()
    return render_template("exhibitor.html",exhibitor_data=exhibitor_data,industry_data=industry_data,state_data=state_data,country_data=country_data)

@app.route("/delete_exhibitor/<int:exhibitor_id>")
def delete_exhibitor(exhibitor_id):
    delete_functions.delete_exhibitor(exhibitor_id)
    return redirect("/exhibitor")

@app.route("/update_exhibitor/<int:exhibitor_id>/<string:exhibitor_name>/<string:email_id>/<string:phone_no>/<string:company_name>/<string:company_description>/<string:company_addr>/<int:company_pin_code>/<string:industry_name>/<string:state_name>/<string:country_name>",methods=['GET','POST'])
def update_exhibitor(exhibitor_id,exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_name,state_name,country_name):
    if(request.method=='POST'):
        update_functions.update_exhibitor(exhibitor_id,request.form['exhibitor_name'],request.form['email_id'],request.form['phone_no'],request.form['company_name'],request.form['company_description'],request.form['company_addr'],request.form['company_pin_code'],request.form['industry_name'],request.form['state_name'],request.form['country_name'])
        return redirect("/exhibitor")
    industry_data = display_functions.display_industry()
    state_data=display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template("update_exhibitor.html",industry_data=industry_data,state_data=state_data,country_data=country_data,exhibitor_id=exhibitor_id,exhibitor_name=exhibitor_name,email_id=email_id,phone_no=phone_no,company_name=company_name,company_description=company_description,company_addr=company_addr,company_pin_code=company_pin_code,industry_name=industry_name,state_name=state_name,country_name=country_name)

