import os
import datetime
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/book_reviews")
def book_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("book_power.html", reviews=reviews)


@app.route("/the_secret_book")
def the_secret_book():
    reviews = mongo.db.reviews_2.find()
    return render_template("the_secret.html", reviews=reviews)


@app.route("/edit_post")
def edit_post():
    reviews = mongo.db.reviews.find()
    return render_template("edit_power.html", reviews=reviews)


@app.route("/delete_post")
def delete_post():
    reviews = mongo.db.reviews.find()
    return render_template("edit_power.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").capitalize()})
        existing_email = mongo.db.users.find_one(
            {"email_address": request.form.get("email_address")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        if existing_email:
            flash("Email Address already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").capitalize(),
            "email_address": request.form.get("email_address"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").capitalize()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").capitalize()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").capitalize()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username).capitalize()

        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    return render_template("add_review.html")


@app.route("/book_power", methods=["GET", "POST"])
def book_power():
    if request.method == "POST":
        review = {
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y"),
            "ratings": request.form.get("ratings")
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("book_reviews"))
        
        reviews = list(mongo.db.reviews.find())
    return render_template("book_power.html")


@app.route("/the_secret", methods=["GET", "POST"])
def the_secret():
    if request.method == "POST":
        the_secret_review = {
            "headline": request.form.get("headline"),
            "the_secret_review": request.form.get("the_secret_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_2.insert_one(the_secret_review)
        flash("Review Successfully Added")
        return redirect(url_for("the_secret_book"))
        
        reviews_2 = list(mongo.db.reviews_2.find())
    return render_template("the_secret.html")


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    edit = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews.find().sort("reviews", 1)
    return render_template(
        "edit_power.html", edit=edit, reviews=reviews)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("book_reviews"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
