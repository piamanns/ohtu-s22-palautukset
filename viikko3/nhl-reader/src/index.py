import requests
from datetime import datetime
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict["goals"],
            player_dict['team']
        )

        players.append(player)

    nationality = "FIN"
    print(f"\nPlayers from {nationality} {datetime.now()}")
    print()

    players_filtered = filter(lambda p : p.nationality == nationality, players)
    for player in sorted(players_filtered, key=lambda p: p.goals+p.assists,
                            reverse=True):
        print(player)

if __name__ == "__main__":
    main()
