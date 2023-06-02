# models/comparisons.py
from .db import db, environment, SCHEMA

class Comparison(db.Model):
    __tablename__ = 'comparisons'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    comparison_id = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, db.ForeignKey('players.player_id'))
    player2_id = db.Column(db.Integer, db.ForeignKey('players.player_id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('players.player_id'))
    comparison_timestamp = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'comparison_id': self.comparison_id,
            'player1_id': self.player1_id,
            'player2_id': self.player2_id,
            'winner_id': self.winner_id,
            'comparison_timestamp': self.comparison_timestamp
        }
