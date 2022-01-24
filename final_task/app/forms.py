from flask_wtf import FlaskForm
from sources.vk import VKSource
from wtforms import DateField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional


class WallGrabForm(FlaskForm):
    choices = VKSource.available_fields
    owner_id = StringField(label="Owner ID *", validators=[DataRequired()])
    fields_list = SelectMultipleField(label="Fields *",
                                      default=choices,
                                      choices=choices,
                                      validators=[DataRequired()])
    start_date = DateField(label="Start Date", validators=[Optional()])
    submit = SubmitField('Grab it')
