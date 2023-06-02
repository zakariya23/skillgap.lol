# models/champion_stats.py
from .db import db, environment, SCHEMA

class ChampionStats(db.Model):
    __tablename__ = 'champion_stats'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    champion_stats_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'))
    champion_id = db.Column(db.Integer, nullable=False)
    champion_name = db.Column(db.String, nullable=False)
    champion_points = db.Column(db.Integer, nullable=False)
    champion_level = db.Column(db.Integer, nullable=False)
    champion_mastery_score = db.Column(db.Integer, nullable=False)
    last_play_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'champion_stats_id': self.champion_stats_id,
            'player_id': self.player_id,
            'champion_id': self.champion_id,
            'champion_name': self.champion_name,
            'champion_points': self.champion_points,
            'champion_level': self.champion_level,
            'champion_mastery_score': self.champion_mastery_score,
            'last_play_time': self.last_play_time
        }


