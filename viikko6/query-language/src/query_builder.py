from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matchers=None, new_rule=None, operator=And):
        self._matchers = matchers if matchers else []
        if new_rule:
            self._matchers.append(new_rule)
        self._logical_operator = operator

    def playsIn(self, team:str):
        return QueryBuilder(self._matchers, PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._matchers, HasAtLeast(value, attr))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._matchers, HasFewerThan(value, attr))

    def oneOf(self, m1, m2):
        return QueryBuilder([m1, m2], None, Or)

    def build(self):
        if len(self._matchers) == 0:
            self._matchers.append(All())
        matcher = self._logical_operator(*self._matchers)
        return matcher
