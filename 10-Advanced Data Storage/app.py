# 1. Import Dependancies and Flask #
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import distinct
from sqlalchemy import and_
import numpy as np
import pandas as pd
import datetime as dt

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()


# 2. Flask Setup #
app = Flask(__name__)


# 3. Set up Flask routes #
@app.route("/")
def home():
    return (
        f"Welcome to Hawaii's Climate API!!!<br/><br/>"
        f"Avalable Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
	last_12_months = session.query(func.max(Measurement.date)).first()
	last_12_months = [r for r in last_12_months]
	Last_dates = dt.datetime.strptime(last_12_months[0], '%Y-%m-%d')
	year_before = Last_dates - dt.timedelta(days=365)

	query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_before).all()
	query_dict = {date: prcp for date, prcp in query}
	return jsonify(query_dict)

@app.route("/api/v1.0/stations")
def stations():
	most_active_stations = session.query(Station.station,).all()
	stations = list(np.ravel(most_active_stations))
	return jsonify(stations)
    
@app.route("/api/v1.0/tobs")
def tobs():
	last_12_months = session.query(func.max(Measurement.date)).first()
	last_12_months = [r for r in last_12_months]
	last_dates = dt.datetime.strptime(last_12_months[0], '%Y-%m-%d')
	year_before = last_dates - dt.timedelta(days=365)
	tobs_query = session.query(Measurement.tobs).filter(Measurement.date >= year_before).all()
	tobs = list(np.ravel(tobs_query))
	return jsonify(tobs)                 

    
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def range_temp(start=None, end=None):

	if end:
		temp_data=calc_temps(start, end)
	else:
		temp_data=calc_temps(start, start)
	return jsonify(temp_data)


# 4. Define main behavior #
if __name__ == "__main__":
    app.run(debug=True)
