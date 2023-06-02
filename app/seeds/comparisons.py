from app.models import db, Player, PlayerStats, Comparison, ChampionStats, SCHEMA, environment
from datetime import datetime
from sqlalchemy.sql import text


def seed_comparisons():
    comparison1 = Comparison(
        player1_id=1,
        player2_id=2,
        winner_id=1,
        comparison_timestamp=datetime.utcnow()
    )

    db.session.add(comparison1)
    db.session.commit()


def undo_comparisons():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.comparisons RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comparisons"))

    db.session.commit()
