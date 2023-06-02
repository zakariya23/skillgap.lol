# forms/comparison_form.py
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class ComparisonForm(FlaskForm):
    player1_id = IntegerField('Player 1 ID', validators=[DataRequired()])
    player2_id = IntegerField('Player 2 ID', validators=[DataRequired()])
    winner_id = IntegerField('Winner ID', validators=[DataRequired()])
    comparison_timestamp = DateTimeField('Comparison Timestamp', validators=[DataRequired()])
    submit = SubmitField('Submit')
