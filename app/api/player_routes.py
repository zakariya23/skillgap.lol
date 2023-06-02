# routes/player_routes.py
from flask import Blueprint, jsonify, request
from app.models import db, Player, PlayerStats, ChampionStats
from riot_api import get_summoner_by_name

player_routes = Blueprint('players', __name__)

# Get all players
@player_routes.route('/')
def get_all_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

# Get a specific player by ID
@player_routes.route('/<int:player_id>')
def get_player(player_id):
    player = Player.query.get(player_id)
    if player:
        return jsonify(player.to_dict())
    else:
        return jsonify({'error': 'Player not found'}), 404

# Get player stats by player ID
@player_routes.route('/<int:player_id>/stats')
def get_player_stats(player_id):
    stats = PlayerStats.query.filter_by(player_id=player_id).all()
    return jsonify([stat.to_dict() for stat in stats])

# Get champion stats by player ID
@player_routes.route('/<int:player_id>/champion_stats')
def get_champion_stats(player_id):
    champ_stats = ChampionStats.query.filter_by(player_id=player_id).all()
    return jsonify([stat.to_dict() for stat in champ_stats])

# You can add more routes to create, update, or delete players and their stats

# Get a player by summoner name
@player_routes.route('/by_summoner_name/<string:summoner_name>')
def get_player_by_summoner_name(summoner_name):
    region = request.args.get('region', 'na1')  # Default to 'na1' if region not provided
    summoner_data = get_summoner_by_name(region, summoner_name)
    if summoner_data.get('status', {}).get('status_code') == 404:
        return jsonify({'error': 'Summoner not found'}), 404
    player = Player.query.filter_by(summoner_id=summoner_data['id']).first()
    if player:
        return jsonify(player.to_dict())
    else:
        return jsonify({'error': 'Player not found'}), 404


# example response: {'id': 'V_ZyXgwuS9suR7-9r5grv1G3Il0dWbUEQUGOs6NhhrTi1knLem-tgA_GfA',
# 'accountId': 'zWvJDhaxbIbo8PdnH-QX0J-48vDzZAc5IXxlYsg_77V-dk3IMlhtbdLY',
# 'puuid': 'wDqMG5GPLwynZRH4m3_wX2t2UyPLcDT36iYeeJ7Gshp-v74OnT6trJv1ftfsZOnIkqrP-dUWsbS8dQ',
# 'name': 'NoohSack', 'profileIconId': 1114, 'revisionDate': 1682211290000, 'summonerLevel': 75}
