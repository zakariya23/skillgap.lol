from flask.cli import AppGroup
from .users import seed_users, undo_users
from .champion_stats import seed_champion_stats, undo_champion_stats
from .comparisons import seed_comparisons, undo_comparisons
from .player_stats import seed_player_stats, undo_player_stats
from .players import seed_players, undo_players
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_champion_stats()
        undo_comparisons()
        undo_player_stats()
        undo_players()
        undo_users()
    seed_users()
    seed_players()
    seed_player_stats()
    seed_comparisons()
    seed_champion_stats()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_champion_stats()
    undo_comparisons()
    undo_player_stats()
    undo_players()
    undo_users()
    # Add other undo functions here
