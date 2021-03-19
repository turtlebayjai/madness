#!/usr/bin/env python3

import argparse
import json

from bracket import Bracket
from division import Division
from team import Team


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("JSON", help="filepath to divisions & teams (JSON file)")
    parser.add_argument("-q", "--quiet", help="only print final winner", action="store_true")
    return parser.parse_args()


def getOrderedTeams(division_dict):
    orderedTeams = []
    for team_dict in division_dict["orderedTeams"]:
        t = Team(team_dict["seed"], team_dict["name"])
        orderedTeams.append(t)
    return orderedTeams


def getOrderedDivisions(data_dict):
    orderedDivisions = []
    for division_dict in data_dict:
        orderedTeams = getOrderedTeams(division_dict)
        d = Division(orderedTeams, division_dict["name"])
        orderedDivisions.append(d)
    return orderedDivisions


def main():
    args = cli()
    with open(args.JSON, "r") as f:
        orderedDivisions = getOrderedDivisions(json.load(f))
    
    bracket = Bracket(orderedDivisions)
    winner = bracket.simulate(args.quiet)
    print(f"Winner: {winner}")


if __name__ == "__main__":
    main()
