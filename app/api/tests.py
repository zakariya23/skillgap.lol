# test_riot_api.py
from riot_api import get_summoner_by_name

def main():
    region = 'na1'  # You can replace this with the desired region
    summoner_name = 'NoohSack'  # Replace this with a valid summoner name
    
    result = get_summoner_by_name(region, summoner_name)
    print(result)

if __name__ == '__main__':
    main()
