# import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# set up flask
app = Flask(__name__)

# use flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_app"
mogno = PyMongo(app)

# define the route for the HTML page
@app.route("/") # this route tells Flask what to display when we are looking at the home page index.html
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# define the route for the 'button' that will scrape updated data when we tell it to
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()