#!/usr/bin/env python3

import argparse
import json

from bracket import Bracket
from picker import Picker
import reader


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("JSON", help="filepath to divisions & teams (JSON file)")
    parser.add_argument(
        "-q", "--quiet", help="only print final winner", action="store_true"
    )
    return parser.parse_args()


def main():
    args = cli()
    divisions = reader.getDataFromJSON(args.JSON)
    bracket = Bracket(divisions, Picker("simpleSeed"))
    winner = bracket.simulate(args.quiet)
    print(f"Winner: {winner}")


if __name__ == "__main__":
    main()
