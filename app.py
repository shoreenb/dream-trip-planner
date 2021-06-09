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
    return render_template("itineraries/itinerary.html", itinerarys=itinerarys)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    itinerarys = list(mongo.db.itinerarys.find({"$text": {"$search": query}}))
    return render_template("itineraries/itinerary.html", itinerarys=itinerarys)


@app.route("/get_home")
def get_home():
    return render_template("pages/navbar/home.html")


@app.route("/get_destinations_info")
def get_destinations_info():
    return render_template("pages/destinations_info.html")


@app.route("/city")
def city():
    return render_template("pages/trip_types/city.html")


@app.route("/beach")
def beach():
    return render_template("pages/trip_types/beach.html")


@app.route("/family")
def family():
    return render_template("pages/trip_types/family.html")


@app.route("/ski")
def ski():
    return render_template("pages/trip_types/ski.html")


@app.route("/register", methods=["GET", "POST"])
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
                "first": request.form.get("first"),
                "last": request.form.get("last"),
                "date_created": datetime.utcnow()
            }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash(
            "Registration Successful!",
            "Thank you for registering with Dream Trip Planner"
            )
        return redirect(url_for("get_account", username=session["user"]))

    return render_template("pages/navbar/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"],
                request.form.get("password")):
                session["user"] = request.form.get("username").lower()

                flash("Welcome, {}".format(
                    request.form.get("username")))

                return redirect(url_for(
                    "get_account",
                    username=session["user"])
                    )

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/navbar/login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # retrieve the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("pages/navbar/account.html", username=username)

    return redirect(url_for("login"))


@app.route("/get_account", methods=["GET", "POST"])
def get_account():
    itinerarys = list(
        mongo.db.itinerarys.find(
            {"created_by": session["user"]}
            )
        )
    user = mongo.db.users.find_one({"username": session["user"]})

    return render_template(
        "pages/navbar/account.html",
        user=user,
        itinerarys=itinerarys
        )


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
    return render_template(
        "itineraries/add_itinerary.html",
        categories=categories,
        countries=countries,
        cities=cities
        )


@app.route("/edit_itinerary/<itinerary_id>", methods=["GET", "POST"])
def edit_itinerary(itinerary_id):
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
        mongo.db.itinerarys.update({"_id": ObjectId(itinerary_id)}, item)
        flash("Itinerary Successfully Updated")

    itinerary = mongo.db.itinerarys.find_one({"_id": ObjectId(itinerary_id)})

    categories = mongo.db.categories.find().sort("categories", 1)
    countries = mongo.db.countries.find().sort("countries", 1)
    cities = mongo.db.cities.find().sort("cities", 1)

    return render_template(
        "itineraries/edit_itinerary.html",
        itinerary=itinerary,
        categories=categories,
        countries=countries,
        cities=cities)


@app.route("/delete_itinerary/<itinerary_id>")
def delete_itinerary(itinerary_id):
    mongo.db.itinerarys.remove({"_id": ObjectId(itinerary_id)})
    flash("Itinerary Successfully Deleted")
    return redirect(url_for("get_itinerarys"))


@app.route("/get_cities")
def get_cities():
    cities = list(mongo.db.cities.find().sort("name", 1))
    return render_template("admin/destinations.html", cities=cities)


@app.route("/admin")
def admin():
    all_itineraries = list(mongo.db.itinerarys.find())
    user_itineraries = list(mongo.db.itinerarys.find({
        "username": session["user"]
    }))

    return render_template(
        "itineraries/itinerary.html",
        all_itineraries=all_itineraries,
        user_itineraries=user_itineraries
    )


@app.route("/add_cities", methods=["GET", "POST"])
def add_cities():
    if request.method == "POST":
        city = {
            "country": request.form.get("country"),
            "name": request.form.get("name")
        }
        mongo.db.cities.insert_one(city)
        flash("New Destination Added")
        return redirect(url_for("get_cities"))

    countries = mongo.db.countries.find().sort("country", 1)
    cities = mongo.db.cities.find().sort("name", 1)
    return render_template(
        "admin/add_destination.html",
        countries=countries,
        cities=cities)


@app.route("/edit_cities/<city_id>", methods=["GET", "POST"])
def edit_cities(city_id):
    if request.method == "POST":
        item = {
            "country": request.form.get("country"),
            "name": request.form.get("name")
        }
        mongo.db.cities.update({"_id": ObjectId(city_id)}, item)
        flash("Destination Successfully Updated")
        return redirect(url_for("get_cities"))

    city = mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    return render_template("admin/edit_destination.html", city=city)


@app.route("/delete_cities/<city_id>")
def delete_cities(city_id):
    mongo.db.cities.remove({"_id": ObjectId(city_id)})
    flash("Destination Successfully Deleted")
    return redirect(url_for("get_cities"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
