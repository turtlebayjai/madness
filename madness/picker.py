import random


class Picker:
    valid = {
        "simpleSeed",
    }

    def __init__(self, method="simpleSeed"):
        if method not in Picker.valid:
            print(f"{method} method is invalid: defaulting to simpleSeed")
            method = "simpleSeed"
        self.method = method
        self.func = getattr(self, method)

    def pickWinner(self, teamA, teamB):
        return self.func(teamA, teamB)

    def simpleSeed(self, A, B):
        if not A and not B:
            return None
        if not A:
            return B
        if not B:
            return A

        favorite, underdog = A, B
        if A.seed < B.seed:
            favorite, underdog = B, A

        result = random.randint(1, favorite.seed + underdog.seed)
        winner = favorite if result > favorite.seed else underdog
        return winner
