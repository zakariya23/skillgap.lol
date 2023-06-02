import os
import requests

RIOT_API_KEY = os.environ.get('RIOT_API_KEY')
BASE_URL = 'https://{region}.api.riotgames.com'

def get_summoner_by_name(region, summoner_name):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": RIOT_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.json()
