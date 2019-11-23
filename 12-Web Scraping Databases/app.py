# Setup Dependencies
from flask import Flask, render_template, redirect 
import os
import scrape_mars
import pymongo

# Create Flask instance
app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars_app'
client = pymongo.MongoClient(conn)

# Renders index.html in the template folder and retreivs info from mongo
@app.route("/")
def index(): 

    mars_info = client.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

# Route for the scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrape functions
    mars_info = client.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    # return "Scraped!"
    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)