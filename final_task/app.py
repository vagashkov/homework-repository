# -*- coding: utf-8 -*-
import os

from flask import Flask, redirect, render_template, send_file, session, url_for
from flask_wtf import FlaskForm
from sources.vk import VKSource
from wtforms import DateField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN') or '123'


app = Flask(__name__)
app.config.from_object(Config)


def create_app():
    return app


class WallGrabForm(FlaskForm):
    """Input form for wall report parameters."""
    choices = VKSource.available_fields
    owner_id = StringField(label="Owner ID *", validators=[DataRequired()])
    fields_list = SelectMultipleField(label="Fields *",
                                      default=choices,
                                      choices=choices,
                                      validators=[DataRequired()])
    start_date = DateField(label="Start Date", validators=[Optional()])
    submit = SubmitField('Grab it')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WallGrabForm()
    if form.validate_on_submit():
        owner_id = form.owner_id.data
        start_date = form.start_date.data
        fields_list = form.fields_list.data
        cwd = os.getcwd()

        # Build new VKSource object for specified wall
        vk_source = VKSource(owner_id, start_date, fields_list=fields_list)

        # Create CSV-based description of the wall
        # and store  CSV file name in session parameters
        csv_file = cwd + f"/{owner_id}" + ".csv"
        vk_source.process_wall_content(csv_file)
        session["csv_file"] = csv_file

        # Build statistics for posts and store it into session parameters
        details_table = vk_source.get_other_statistics_html()
        session["details_table"] = details_table
        return redirect(url_for('results'))
    return render_template('index.html',
                           title='Simple Wall Grabber', form=form)


@app.route('/results')
def results():
    return render_template("results.html",
                           csv_file=session["csv_file"],
                           posts_table=session["posts_table"],
                           details_table=session["details_table"])


@app.route('/return-files/')
def return_files():
    try:
        csv_file = session["csv_file"]
        return send_file(csv_file, attachment_filename="Wall report")
    except Exception as e:
        return str(e)
