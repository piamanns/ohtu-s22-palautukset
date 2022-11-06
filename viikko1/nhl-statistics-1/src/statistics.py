from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_by(player, key: SortBy):
    if key == SortBy.GOALS:
        return player.goals
    if key == SortBy.ASSISTS:
        return player.assists
    return player.points


class Statistics:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_param=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player : sort_by(player, sort_param)
        )

        result = []
        i = 0

        # cannot list more top scorers than there are players
        how_many = min(how_many, len(sorted_players))

        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
