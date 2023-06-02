from app.models import db, Player, PlayerStats, Comparison, ChampionStats, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import text


def seed_champion_stats():
    champion_stats1 = ChampionStats(
        player_id=1,
        champion_id=1,
        champion_name='Champion1',
        champion_points=1000,
        champion_level=3,
        champion_mastery_score=600,
        last_play_time=datetime.utcnow()
    )

    champion_stats2 = ChampionStats(
        player_id=2,
        champion_id=2,
        champion_name='Champion2',
        champion_points=1500,
        champion_level=4,
        champion_mastery_score=800,
        last_play_time=datetime.utcnow()
    )

    db.session.add(champion_stats1)
    db.session.add(champion_stats2)
    db.session.commit()


def undo_champion_stats():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.champion_stats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM champion_stats"))

    db.session.commit()
