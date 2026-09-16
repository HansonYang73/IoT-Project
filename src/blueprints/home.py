from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from ..db import Db
from src.rpi import success, failure
    
class AddForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    address = StringField('Home Address:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    phone_number = StringField('Phone Number:', validators=[DataRequired()])
    submit = SubmitField("Add")


    
home = Blueprint("home", __name__)

@home.route("/")
def show():
    return render_template("home.html", add_form=AddForm())

@home.route("/create", methods=["GET", "POST"])
def create():
    form = AddForm()
    if form.validate_on_submit():
        # Get form values
        name = request.form["name"]
        address = request.form["address"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        
        db = Db.get_instance()
        status = db.add_customer(name, address, email, phone_number)
        if status == 0:
            success()
        else:
            failure()

        return redirect(url_for("home.show"))

    return render_template("home.html", add_form=AddForm())

