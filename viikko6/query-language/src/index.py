from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, Or, Not, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print("---")

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )
    
    for player in stats.matches(matcher):
        print(player)
    
    print("---")


    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)
    
    print("---")

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher):
        print(player)

    print("---")

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)

    print("---")

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

if __name__ == "__main__":
    main()
