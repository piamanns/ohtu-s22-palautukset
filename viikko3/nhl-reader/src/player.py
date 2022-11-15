class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
    
    def __str__(self):
        return (
            f"{self.name:20} {self.team} "
            f"{self.goals:2} + {self.assists:2} "
            f"= {self.goals+self.assists:2}"
        )
