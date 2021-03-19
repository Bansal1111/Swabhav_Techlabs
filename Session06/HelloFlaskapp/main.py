from flask import  Flask,jsonify,abort
from datetime import  datetime
from model import db



app=Flask(__name__)
@app.route("/")
def hello_world():
    return f"""
        <h1>
        Hello from Flask App {datetime.now()}
        </h1>
        """
@app.route("/api/v1/employees")
def get_employees():
    return jsonify(db)

@app.route("/api/v1/employees/<int:emp_index>")
def get_emp(emp_index):
    try:
        return db[emp_index]
    except IndexError:
        abort(404)