from .db import db, environment, SCHEMA

class Player(db.Model):
    __tablename__ = 'players'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    player_id = db.Column(db.Integer, primary_key=True)
    summoner_id = db.Column(db.String, nullable=False, unique=True)
    summoner_name = db.Column(db.String, nullable=False)
    account_id = db.Column(db.String, nullable=False, unique=True)
    region = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'summoner_id': self.summoner_id,
            'summoner_name': self.summoner_name,
            'account_id': self.account_id,
            'region': self.region
        }
