class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
    
    def __str__(self):
        return f"{self.name} team {self.team}, goals {self.goals} assists {self.assists}"
