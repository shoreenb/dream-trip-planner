import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_itinerarys")
def get_itinerarys():
    itinerarys = list(mongo.db.itinerarys.find())
    return render_template("itinerary.html", itinerarys=itinerarys)


@app.route("/get_home")
def get_home():
    return render_template("home.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
     
        if existing_user:
            flash("Sorry, this username already exists!")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if password != confirm_password:
            flash("Those passwords do not match")
            return redirect(url_for("register"))

        if password == confirm_password:

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "first": request.form.get("first").upper(),
                "last": request.form.get("last").upper(),
                "date_created": datetime.utcnow()
            }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", "Thank you for registering with Dream Trip Planner")
        return redirect(url_for("get_account", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "get_account", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# @app.before_request
# def before_request():
#     loggedIn = True if 'user' in session else False
#     if session["user"] == loggedIn:
#         session["user"].last_seen = datetime.utcnow()
#         db.session.commit()


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # retrieve the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
 
    if session["user"]:
        return render_template("account.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/get_account", methods=["GET", "POST"])
def get_account():
    if request.method == "POST":
        profile = {
            "username": request.form.get("username"),
            "first": request.form.get("first").upper(),
            "last": request.form.get("last").upper(),
            "date_created": datetime.utcnow()
        }
        mongo.db.users.insert_one(profile)
        flash("Account Successfully Added")
        return redirect(url_for("get_account"))

    itinerarys = list(mongo.db.itinerarys.find())
    users = list(mongo.db.users.find())
    return render_template("account.html", itinerarys=itinerarys, users=users)


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_itinerary", methods=["GET", "POST"])
def add_itinerary():
    if request.method == "POST":
        item = {
            "trip_name": request.form.get("trip_name"),
            "date": request.form.get("date"),
            "countries": request.form.get("countries"),
            "cities": request.form.get("cities"),
            "categories": request.form.get("categories"),
            "activity_name": request.form.get("activity_name"),
            "day": request.form.get("day"),
            "time": request.form.get("time"),
            "duration": request.form.get("duration"),
            "item_description": request.form.get("item_description"),
            "created_by": session["user"],
            "date_created": datetime.utcnow(),
            "last_updated": datetime.now()
        }
        mongo.db.itinerarys.insert_one(item)
        flash("Itinerary Successfully Added")
        return redirect(url_for("get_itinerarys"))

    categories = mongo.db.categories.find().sort("categories", 1)
    countries = mongo.db.countries.find().sort("countries", 1)
    cities = mongo.db.cities.find().sort("cities", 1)
    return render_template("add_itinerary.html", categories=categories, 
        countries=countries, cities=cities)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
