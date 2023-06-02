from app.models import db, Player, PlayerStats, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import text

def seed_players():
    player1 = Player(
        summoner_id='sample_summoner_id_1',
        summoner_name='PlayerOne',
        account_id='sample_account_id_1',
        region='NA'
    )

    player2 = Player(
        summoner_id='sample_summoner_id_2',
        summoner_name='PlayerTwo',
        account_id='sample_account_id_2',
        region='NA'
    )

    db.session.add(player1)
    db.session.add(player2)
    db.session.commit()


def undo_players():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM players"))

    db.session.commit()
