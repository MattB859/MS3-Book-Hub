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

    """
    map routing for home page
    """
    return render_template("home.html")


@app.route("/user_admin")
def user_admin():

    """
    find the user in the database
    """
    users = mongo.db.users.find()
    return render_template("delete_user.html", users=users)


@app.route("/book_reviews")
def book_reviews():

    """
    Code by the developer.
    Find the list of reviews in the database to view
    """
    reviews = mongo.db.reviews.find()
    return render_template("book_power.html", reviews=reviews)


@app.route("/the_secret_book")
def the_secret_book():

    """
    Code by the developer.
    Find the list of reviews_2 in the database to view
    """
    reviews = mongo.db.reviews_2.find()
    return render_template("the_secret.html", reviews=reviews)


@app.route("/power_of_now")
def power_of_now():

    """
    Code by the developer.
    Find the list of reviews_3 in the database to view
    """
    reviews = mongo.db.reviews_3.find()
    return render_template("the_power_of_now.html", reviews=reviews)


@app.route("/the_alchemist")
def the_alchemist():

    """
    Code by the developer.
    Find the list of reviews_4 in the database
    """
    reviews = mongo.db.reviews_4.find()
    return render_template("alchemist_book.html", reviews=reviews)


@app.route("/edit_post")
def edit_post():

    """
    Code by the developer.
    Find the list of reviews in the database
    """
    reviews = mongo.db.reviews.find()
    return render_template("edit_power.html", reviews=reviews)


@app.route("/edit_secret_post")
def edit_secret_post():

    """
    Code by the developer.
    Find the list of reviews_2 in the database
    """
    reviews = mongo.db.reviews_2.find()
    return render_template("edit_secret.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():

    """
    Code source from code institute tutorial.
    check if username already exists in the database
    """
    if request.method == "POST":
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

        register_user = {
            "username": request.form.get("username").capitalize(),
            "email_address": request.form.get("email_address"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").capitalize()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    """
    Code source from code institute tutorial.
    Grab the session user's username from db
    """
    if request.method == "POST":
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

    """
    Code source from code institute tutorial and edited
    by the developer.
    Grab the session user's username from db
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = mongo.db.reviews.find()
    views = mongo.db.reviews_2.find()
    posts = mongo.db.reviews_3.find()
    al_posts = mongo.db.reviews_4.find()

    return render_template(
        "profile.html", reviews=reviews, posts=posts, views=views,
        al_posts=al_posts, username=username)


@app.route("/logout")
def logout():

    """
    Remove user from session cookie
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():

    """
    Code by the developer.
    map routing for add reviews page
    """
    return render_template("add_review.html")


@app.route("/book_power", methods=["GET", "POST"])
def book_power():

    """
    Code by the developer,
    allows users to create and add reviews
    """
    if request.method == "POST":
        review = {
            "title": "The 48 Laws Of Power",
            "author": "Robert Greene",
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("book_reviews"))

    return render_template("book_power.html")


@app.route("/the_secret", methods=["GET", "POST"])
def the_secret():

    """
    Code by the developer,
    allows users to create and add reviews
    """
    if request.method == "POST":
        the_secret_review = {
            "title": "The Secret",
            "author": "Rhonda Byrne",
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_2.insert_one(the_secret_review)
        flash("Review Successfully Added")
        return redirect(url_for("the_secret_book"))

    return render_template("the_secret.html")


@app.route("/the_power_of", methods=["GET", "POST"])
def the_power_of():

    """
    Code by the developer,
    allows users to create and add reviews
    """
    if request.method == "POST":
        the_secret_review = {
            "title": "The Power Of Now",
            "author": "Tolle Eckhart ",
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_3.insert_one(the_secret_review)
        flash("Review Successfully Added")
        return redirect(url_for("power_of_now"))

    return render_template("the_power_of_now.html")


@app.route("/the_alchemist_book", methods=["GET", "POST"])
def the_alchemist_book():

    """
    Code by the developer,
    allows users to create and add reviews
    """
    if request.method == "POST":
        review = {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_4.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("the_alchemist"))

    return render_template("alchemist_book.html")


@app.route("/edit_alchemist/<review_id>", methods=["GET", "POST"])
def edit_alchemist(review_id):

    """
    Code by the developer,
    allows users to edit their reviews
    """
    if request.method == "POST":
        submit = {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_4.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for("the_alchemist"))

    edit = mongo.db.reviews_4.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews_4.find().sort("reviews", 1)
    return render_template("edit_alchemist.html",  edit=edit, reviews=reviews)


@app.route("/edit_the_power_of/<review_id>", methods=["GET", "POST"])
def edit_the_power_of(review_id):

    """
    Code by the developer,
    allows users to edit their reviews
    """
    if request.method == "POST":
        submit = {
            "title": "The Power Of Now",
            "author": "Tolle Eckhart ",
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_3.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for("power_of_now"))

    edit = mongo.db.reviews_3.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews_3.find().sort("reviews", 1)
    return render_template(
        "edit_the_power_of_now.html", edit=edit, reviews=reviews)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):

    """
    Code by the developer,
    allows users to edit their book reviews
    """
    if request.method == "POST":
        submit = {
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for("book_reviews"))

    edit = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews.find().sort("reviews", 1)
    return render_template(
        "edit_power.html,", edit=edit, reviews=reviews)


@app.route("/edit_secret/<review_id>", methods=["GET", "POST"])
def edit_secret(review_id):

    """
    Code by the developer,
    allows a user to edit 'the secret' book reviews
    """
    if request.method == "POST":
        submit = {
            "headline": request.form.get("headline"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"],
            "date_time": datetime.datetime.now().strftime("%d %B %Y")
        }
        mongo.db.reviews_2.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for("the_secret_book"))

    edit = mongo.db.reviews_2.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews_2.find().sort("reviews", 1)
    return render_template(
        "edit_secret.html", edit=edit, reviews=reviews)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):

    """
    Code by the developer,
    allows user to delete 'the 48 laws of power' reviews
    """
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("book_reviews"))


@app.route("/delete_review_2/<review_id>")
def delete_review_2(review_id):

    """
    Code by the developer,
    allows user to delete 'the secret' reviews
    """
    mongo.db.reviews_2.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("the_secret_book"))


@app.route("/delete_review_3/<review_id>")
def delete_review_3(review_id):

    """
    Code by the developer,
    allows user to delete 'the power of now' reviews
    """
    mongo.db.reviews_3.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("power_of_now"))


@app.route("/delete_review_4/<review_id>")
def delete_review_4(review_id):

    """
    Code by the developer,
    allows user to delete their reviews
    """
    mongo.db.reviews_4.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("the_alchemist"))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):

    """
    Code by the developer,
    allows users to delete their user account
    """
    if session["user"]:
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        flash("User Successfully Deleted")
        session.pop("user")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
