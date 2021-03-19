from collections import deque
from math import ceil, log

from division import Division
from picker import Picker


class BracketNode:
    def __init__(self, team=None, left=None, right=None):
        self.team = team
        self.left = left
        self.right = right

    def play(self, picker):
        if not self.left and not self.right:
            return self.team

        leftWinner = rightWinner = None
        if self.left:
            leftWinner = self.left.play(picker)
        if self.right:
            rightWinner = self.right.play(picker)
        self.team = picker.pickWinner(leftWinner, rightWinner)
        return self.team

    def __str__(self):
        string = ""
        queue = deque([self])
        while queue:
            roundResult = "\n"
            for i in range(len(queue)):
                node = queue.popleft()
                roundResult += str(node.team) + "  |  "
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            string += roundResult + "\n" + ("--" * 40)
        return string


class Bracket:
    def __init__(self, orderedDivisions, picker=None):
        """
        orderedDivisions = [
            Division (object),
            Division (object),
            ...
        ],
        picker: Picker (object)
        """
        self.orderedDivisions = orderedDivisions
        if not picker:
            picker = Picker("simpleSeed")
        self.picker = picker

    def build(self, division):
        leaves = deque(division.orderedTeams)

        levels = int(ceil(log(len(leaves), 2)))
        root = BracketNode()
        queue = deque([root])
        for i in range(levels - 1):
            for j in range(len(queue)):
                node = queue.popleft()
                node.left, node.right = BracketNode(), BracketNode()
                queue.append(node.left)
                queue.append(node.right)

        while queue:
            node = queue.popleft()
            node.left = BracketNode(team=leaves.popleft())
            node.right = BracketNode(team=leaves.popleft())
        return root

    def simulate(self, quiet=False):
        finalTeams = []
        for division in self.orderedDivisions:
            root = self.build(division)
            finalTeams.append(root.play(self.picker))
            if not quiet:
                print(f"\n* {division.name} *")
                print(root)

        if not finalTeams:
            return None

        winner = finalTeams[0]
        if len(finalTeams) > 1:
            finals = Division(finalTeams, "Finals")
            root = self.build(finals)
            winner = root.play(self.picker)
            if not quiet:
                print(f"\n* {finals.name} *")
                print(root)

        return winner
