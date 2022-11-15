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

    for player in players:
        if player.nationality == nationality:
            print(player)

if __name__ == "__main__":
    main()
