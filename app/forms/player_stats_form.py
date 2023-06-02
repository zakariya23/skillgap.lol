# forms/player_stats_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class PlayerStatsForm(FlaskForm):
    player_id = IntegerField('Player ID', validators=[DataRequired()])
    queue_type = StringField('Queue Type', validators=[DataRequired(), Length(max=255)])
    tier = StringField('Tier', validators=[DataRequired(), Length(max=255)])
    rank = StringField('Rank', validators=[DataRequired(), Length(max=255)])
    league_points = IntegerField('League Points', validators=[DataRequired(), NumberRange(min=0)])
    wins = IntegerField('Wins', validators=[DataRequired(), NumberRange(min=0)])
    losses = IntegerField('Losses', validators=[DataRequired(), NumberRange(min=0)])
    win_rate = FloatField('Win Rate', validators=[DataRequired(), NumberRange(min=0, max=100)])
    kda = FloatField('KDA', validators=[DataRequired(), NumberRange(min=0)])
    cs_per_min = FloatField('CS per Minute', validators=[DataRequired(), NumberRange(min=0)])
    update_timestamp = DateTimeField('Update Timestamp', validators=[DataRequired()])
    submit = SubmitField('Submit')
