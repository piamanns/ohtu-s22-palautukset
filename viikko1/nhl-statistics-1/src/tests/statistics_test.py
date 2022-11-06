import unittest
from statistics import Statistics
from statistics import SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
  
    def test_constructor_creates_list_of_players(self):
        self.assertEqual(len(self.statistics._players), 5)
    
    def test_search_returns_correct_player_if_player_is_on_list(self):
        player = self.statistics.search("Lemieux")

        self.assertEqual("Lemieux", player.name)
        self.assertEqual("PIT", player.team)
        self.assertEqual(45, player.goals)
        self.assertEqual(54, player.assists)
    
    def test_search_returns_None_if_player_is_not_on_list(self):
        player = self.statistics.search("Koivu")

        self.assertEqual(None, player)

    def test_team_returns_correct_players(self):
        team = self.statistics.team("EDM")

        self.assertEqual(len(team), 3)
        self.assertEqual(team[0].name, "Semenko")
        self.assertEqual(team[1].name, "Kurri")
        self.assertEqual(team[2].name, "Gretzky")

        for i in range(len(team)):
            self.assertEqual(team[i].team, "EDM")

    def test_team_returns_empty_list_if_team_does_not_exists(self):
        team = self.statistics.team("FOO")

        self.assertEqual(len(team), 0)
    
    def test_top_returns_right_amount_of_top_players(self):
        top = self.statistics.top(3)
        self.assertEqual(len(top), 3)
    
    def test_top_returns_empty_list_if_given_top_player_amount_is_negative(self):
        top = self.statistics.top(-2)
        self.assertEqual(len(top), 0)

    def test_top_returns_available_number_of_players_if_given_count_is_larger(self):
        top = self.statistics.top(10)
        self.assertEqual(len(top), 5)

    def test_top_without_sort_param_returns_correct_players_in_right_order(self):
        top = self.statistics.top(3)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_with_points_as_sort_param_returns_correct_players_in_right_order(self):
        top = self.statistics.top(3, SortBy.POINTS)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_with_goals_as_sort_param_returns_correct_players_in_right_order(self):
        top = self.statistics.top(3, SortBy.GOALS)

        self.assertEqual(top[0].name, "Lemieux")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Kurri")
   
    def test_top_with_assists_as_sort_param_returns_correct_players_in_right_order(self):
        top = self.statistics.top(3, SortBy.ASSISTS)

        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Lemieux")
