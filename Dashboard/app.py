from flask import Flask, render_template, redirect,jsonify,render_template
app = Flask(__name__)

from sqlalchemy import create_engine
import pandas as pd

# for pandas reqd_sql
engine = create_engine(f"postgresql://postgres:asd@localhost:5432/DAB-Project-2")
connection = engine.connect()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/data")
def data():
    
    df = pd.read_sql("SELECT * FROM airline_crash ",connection)
    records = df.to_json()
    return records


if __name__ == "__main__":
    app.run(debug=True)