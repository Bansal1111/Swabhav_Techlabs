import connect

from flask import  Flask,render_template,request

app=Flask(__name__)
@app.route("/login")
def get_form():
    return render_template('login.html')

@app.route("/login",methods=['POST'])
def get_contact():
    name = request.form['name']
    contact = request.form['contact']
    check = connect.check_user(name,contact)
    if(check == True):
        ans = connect.all_data()
        return render_template('after_login.html',n=name,c=contact,data=ans)
    else:
        return render_template('login.html',c='Failed')


@app.route("/adding_new_contact",methods=['GET'])
def get_new_contact_form():
    return render_template('adding_new_contact.html')
    fname = request.form['fname']
    lname = request.form['lname']
    contact = request.form['contact']
    print(fname)
    connect.add_contact(fname, lname, contact)

@app.route("/adding_new_contact", methods=['POST'])
def get_new_contact():
     fname = request.form['fname']
     lname = request.form['lname']
     contact = request.form['contact']
     connect.add_contact(fname, lname, contact)
     ans = connect.all_data()
     return render_template('after_login.html', data=ans)



