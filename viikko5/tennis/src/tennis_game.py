class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self._p1_points = 0
        self._p2_points = 0
        self._points_to_win = 4
        self._diff_to_win = 2

        self._point_descriptions = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self._p1_points += 1
        else:
            self._p2_points += 1

    def _check_for_win(self, p1_name:str, p1_points:int,
                       p2_name: str, p2_points:int,
                       diff_to_win:int):

        diff = abs(p1_points - p2_points)
        if diff >= diff_to_win:
            winner = p1_name if p1_points > p2_points else p2_name
            return f"Win for {winner}"
        if diff > 0:
            advantage = p1_name if p1_points > p2_points else p2_name
            return f"Advantage {advantage}"
        return "Deuce"
    
    def _get_score(self, p1_points, p2_points):
        if p1_points == p2_points:
            return f"{self._point_descriptions[p1_points]}-All"
        return (f"{self._point_descriptions[p1_points]}"
                f"-{self._point_descriptions[p2_points]}")
  
    def get_score(self):
        if (self._p1_points >= self._points_to_win
            or self._p2_points >= self._points_to_win):
            
            return self._check_for_win(self.p1_name, self._p1_points,
                                       self.p2_name, self._p2_points,
                                       self._diff_to_win)

        return self._get_score(self._p1_points, self._p2_points)
