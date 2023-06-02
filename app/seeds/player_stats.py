from app.models import db, Player, PlayerStats, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import text


def seed_player_stats():
    player1_stats = PlayerStats(
        player_id=1,
        queue_type='RANKED_SOLO_5x5',
        tier='GOLD',
        rank='III',
        league_points=52,
        wins=30,
        losses=24,
        win_rate=55.6,
        kda=3.1,
        cs_per_min=5.7,
        update_timestamp=datetime.utcnow()
    )

    player2_stats = PlayerStats(
        player_id=2,
        queue_type='RANKED_SOLO_5x5',
        tier='SILVER',
        rank='I',
        league_points=89,
        wins=27,
        losses=28,
        win_rate=49.1,
        kda=2.7,
        cs_per_min=6.2,
        update_timestamp=datetime.utcnow()
    )

    db.session.add(player1_stats)
    db.session.add(player2_stats)
    db.session.commit()


def undo_player_stats():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.player_stats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM player_stats"))

    db.session.commit()
