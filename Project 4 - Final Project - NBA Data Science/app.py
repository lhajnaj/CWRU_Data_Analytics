import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

from sklearn.externals import joblib

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# CREATE TABLE players (pk integer PRIMARY KEY NOT NULL,
#   "rk" REAL,
#   "olayer" text,
#   "tm" TEXT,
#   "salary_2019to2020" INTEGER,
#   "salary_2020to2021" TEXT,
#   "salary_2021to2022" TEXT,
#   "salary_2022to2023" TEXT,
#   "salary_2023to2024" TEXT,
#   "salary_2024to2025" TEXT,
#   "signed_using" TEXT,
#   "guaranteed" TEXT,
#   "year_start" INTEGER,
#   "position" TEXT,
#   "height" REAL,
#   "weight" REAL,
#   "birth_date" TIMESTAMP,
#   "college" TEXT,
#   "age" INTEGER,
#   "gp" INTEGER,
#   "w" INTEGER,
#   "l" INTEGER,
#   "min" REAL,
#   "pts" REAL,
#   "fgm" REAL,
#   "fga" REAL,
#   "fg_prc" REAL,
#   "three_pnt_m" REAL,
#   "three_pnt_a" REAL,
#   "three_pnt_prc" REAL,
#   "ftm" REAL,
#   "fta" REAL,
#   "ft_prc" REAL,
#   "oreb" REAL,
#   "dreb" REAL,
#   "reb" REAL,
#   "ast" REAL,
#   "tov" REAL,
#   "stl" REAL,
#   "blk" REAL,
#   "plusminus" REAL);
# sqlite>







app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/nba.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
players = Base.classes.players


@app.route('/', methods=['GET','POST'])
def predict():
    salary = ''
    if request.method == 'POST':
        age = float(request.form["age"])
        pts = float(request.form["pts"])
        reb = float(request.form["reb"])
        ast = float(request.form["ast"])
        plm = float(request.form["plm"])

        # player = Player(age=age, pts=pts, reb=reb, ast=ast, plm=plm)
        # stmt = db.session.query(players).statement
        # df = pd.read_sql_query(stmt, db.session.bind)     
        # query = df.to_json(orient="records")
        data = np.array([age,pts,reb,ast,plm]).reshape(1,-1)
        results = int(clf.predict(data)[0])
        # prediction = clf.predict(data)[0]
        # return jsonify({'prediction':list(prediction)})
        salary = f"${results:,}"

    return render_template("form.html", salary=salary)

    

@app.route("/player_search")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/height")
def index2():
    
    return render_template("index2_height_scatter.html")

@app.route("/age")
def index3():
    
    return render_template("index3_age_scatter.html")

@app.route("/ppg")
def index4():
    
    return render_template("index4_ppg_scatter.html")

@app.route("/plusminus")
def index5():
    
    return render_template("index5_plusminus_scatter.html")

@app.route("/heighthistogram")
def index7():
    
    return render_template("index7_height_histogram.html")

@app.route("/serviceline")
def index8():
    
    return render_template("index8_service_line.html")

@app.route("/stacked")
def index9():
    
    return render_template("index9_team_salary_stacked.html")

@app.route("/player1")  # select * from players
def player1():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(players).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    # return jsonify(list(df.columns)[2:])
    return jsonify(list(df['player']))

@app.route("/player2")  # select * from players
def player2():

    # Use Pandas to perform the sql query
    stmt = db.session.query(players).statement
    df = pd.read_sql_query(stmt, db.session.bind)     
    return df.to_json(orient="records")
    

@app.route("/player3")  # select * from players
def player3():

    # Use Pandas to perform the sql query
    stmt = db.session.query(players).statement
    df = pd.read_sql_query(stmt, db.session.bind)  
    
    return df.to_json()
    
@app.route("/player4")  # select * from players
def player4(): 

    # Use Pandas to perform the sql query
    stmt = db.session.query(players).statement
    df = pd.read_sql_query(stmt, db.session.bind)
  
    df1=df[["player","age"]][0:10]
    return df1.to_json(orient="records")
    
   

if __name__ == "__main__":
    clf = joblib.load('model.pkl')
    app.run()
