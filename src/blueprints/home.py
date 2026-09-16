from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

    
class AddForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
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
        
        # data.create_personne(name)

        return redirect(url_for("home.show"))

    return render_template("home.html", add_form=AddForm())

