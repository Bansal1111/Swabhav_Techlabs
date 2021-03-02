from flask import Flask, redirect, url_for, request, render_template
import connection
from Dashboards import booking
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def home():
    visitor = connection.new_disp_visitor()
    return render_template("new_home.html", data=visitor)


@app.route("/choose_id_or_num")
def choose_id_or_num():
    return render_template("new_choose_id_or_num.html")


@app.route("/get_id", methods=["POST", "GET"])
def get_id():
    if request.method == "POST":
        email = request.form["email"]
        return redirect(url_for("update_data", email=email))
    else:
        email = request.args.get("email")
        return redirect(url_for("update_data", email=email))


@app.route("/update_data/<email>")
def update_data(email):
    return render_template("new_update.html", email=email)


@app.route("/get_name" + "/<email>")
def get_name(email):
    return render_template("new_update_name.html", email=email)


@app.route("/update_name/<email>")
def update_name(email):
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        return redirect(url_for("disp_message", fname=fname, lname=lname, email=email))
    else:
        fname = request.args.get("fname")
        lname = request.args.get("lname")
        return redirect(url_for("disp_message", fname=fname, lname=lname, email=email))


@app.route("/disp_message/<fname>/<lname>/<email>")
def disp_message(fname, lname, email):
    data = connection.update_name(fname, lname, email)
    return render_template("new_disp_message.html", data=data)


@app.route("/booking")
def booking_dashboard():

    return render_template(
        "booking_dash.html",
        name=booking.booking_dash([1, 2, 3], [2, 3, 5]),
        label=["Mon", "Tue", "Wed", "Thu", "Fri"],
        serie=[5, 2, 4, 2, 0],
    )

