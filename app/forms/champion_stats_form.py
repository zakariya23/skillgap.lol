# forms/champion_stats_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ChampionStatsForm(FlaskForm):
    player_id = IntegerField('Player ID', validators=[DataRequired()])
    champion_id = IntegerField('Champion ID', validators=[DataRequired()])
    champion_name = StringField('Champion Name', validators=[DataRequired(), Length(max=255)])
    champion_points = IntegerField('Champion Points', validators=[DataRequired(), NumberRange(min=0)])
    champion_level = IntegerField('Champion Level', validators=[DataRequired(), NumberRange(min=1, max=7)])
    champion_mastery_score = IntegerField('Champion Mastery Score', validators=[DataRequired(), NumberRange(min=0)])
    last_play_time = DateTimeField('Last Play Time', validators=[DataRequired()])
    submit = SubmitField('Submit')
