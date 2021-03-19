class Team:
    def __init__(self, seed, name=None):
        self.seed = seed
        self.name = name

    def __str__(self):
        return f"({self.seed}){self.name}"
