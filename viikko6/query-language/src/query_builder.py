from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan


class QueryBuilder:
    def __init__(self, matchers=[], new_rule=All()):
        self._matchers = matchers
        self._matchers.append(new_rule)

    def playsIn(self, team:str):
        return QueryBuilder(self._matchers, PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._matchers, HasAtLeast(value, attr))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._matchers, HasFewerThan(value, attr))

    def build(self):
        matcher = And(*self._matchers)
        return matcher
