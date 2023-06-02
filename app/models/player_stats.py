from .db import db, environment, SCHEMA, add_prefix_for_prod

class PlayerStats(db.Model):
    __tablename__ = 'player_stats'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    stats_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'))
    queue_type = db.Column(db.String, nullable=False)
    tier = db.Column(db.String, nullable=False)
    rank = db.Column(db.String, nullable=False)
    league_points = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    win_rate = db.Column(db.Float, nullable=False)
    kda = db.Column(db.Float, nullable=False)
    cs_per_min = db.Column(db.Float, nullable=False)
    update_timestamp = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'stats_id': self.stats_id,
            'player_id': self.player_id,
            'queue_type': self.queue_type,
            'tier': self.tier,
            'rank': self.rank,
            'league_points': self.league_points,
            'wins': self.wins,
            'losses': self.losses,
            'win_rate': self.win_rate,
            'kda': self.kda,
            'cs_per_min': self.cs_per_min,
            'update_timestamp': self.update_timestamp
        }
