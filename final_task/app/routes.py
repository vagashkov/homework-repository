# -*- coding: utf-8 -*-
import os

from app import app
from app.forms import WallGrabForm
from flask import redirect, render_template, send_file, session, url_for
from sources.vk import VKSource


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
