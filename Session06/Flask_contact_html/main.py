import connect

from flask import  Flask,render_template

app=Flask(__name__)
@app.route("/contact")
def get_contact():
    ans=connect.all_data()
    return render_template('contact.html',data=ans)
