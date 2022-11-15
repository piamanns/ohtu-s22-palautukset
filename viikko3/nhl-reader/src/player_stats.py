class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = filter(lambda p : p.nationality == nationality,
                                        self.players)
        players_sorted = sorted(players_by_nationality,
                                key=lambda p: p.goals+p.assists,
                                reverse=True)
        return players_sorted
