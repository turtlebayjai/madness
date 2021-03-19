class Division:
    """
    name: string,
    orderedTeams = [
        Team (object), # 1 seed
        Team (object), # 16 seed
        Team (object), # 8 seed
        Team (object), # 9 seed
        ...
        Team (object), # 15 seed
    ]
    """

    def __init__(self, orderedTeams, name=None):
        self.orderedTeams = orderedTeams
        self.name = name
