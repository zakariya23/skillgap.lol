# forms/player_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class PlayerForm(FlaskForm):
    summoner_id = StringField('Summoner ID', validators=[DataRequired(), Length(max=255)])
    summoner_name = StringField('Summoner Name', validators=[DataRequired(), Length(max=255)])
    account_id = StringField('Account ID', validators=[DataRequired(), Length(max=255)])
    region = StringField('Region', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Submit')
