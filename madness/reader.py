import json

from division import Division
from team import Team


def getDataFromJSON(json_path):
    with open(json_path, "r") as f:
        orderedDivisions = _getOrderedDivisions(json.load(f))
    return orderedDivisions


def _getOrderedTeams(division_dict):
    orderedTeams = []
    for team_dict in division_dict["orderedTeams"]:
        t = Team(team_dict["seed"], team_dict["name"])
        orderedTeams.append(t)
    return orderedTeams


def _getOrderedDivisions(data_dict):
    orderedDivisions = []
    for division_dict in data_dict:
        orderedTeams = _getOrderedTeams(division_dict)
        d = Division(orderedTeams, division_dict["name"])
        orderedDivisions.append(d)
    return orderedDivisions
