from collections import deque
from math import ceil, log
import random


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getWinner(A, B):
    if not A and not B:
        return None
    if not A:
        return B
    if not B:
        return A

    favorite = min(A, B)
    underdog = max(A, B)
    result = random.randint(1, favorite + underdog)
    winner = favorite if result > favorite else underdog
    return winner


def buildBracket(leaves):
    levels = int(ceil(log(len(leaves), 2)))
    root = TreeNode()
    queue = deque([root])
    for i in range(levels - 1):
        for j in range(len(queue)):
            node = queue.popleft()
            node.left = TreeNode()
            queue.append(node.left)
            node.right = TreeNode()
            queue.append(node.right)

    leaves = deque(leaves)
    while queue:
        node = queue.popleft()
        node.left = TreeNode(leaves.popleft())
        node.right = TreeNode(leaves.popleft())
    return root


def fillBracket(root):
    if not root.left and not root.right:
        return root.val

    leftWinner = rightWinner = None
    if root.left:
        leftWinner = fillBracket(root.left)
    if root.right:
        rightWinner = fillBracket(root.right)
    root.val = getWinner(leftWinner, rightWinner)
    return root.val


def printBracket(root, division=None):
    if division:
        print(f"\n* {division} *")
    queue = deque([root])
    while queue:
        print("--" * 19)
        roundResult = ""
        for i in range(len(queue)):
            node = queue.popleft()
            roundResult += str(node.val) + " "
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(roundResult)


def simulate(ordering, divisions=[None]):
    finalists = []
    for division in divisions:
        root = buildBracket(ordering)
        finalists.append(fillBracket(root))
        printBracket(root, division)

    if len(finalists) > 1:
        root = buildBracket(finalists)
        fillBracket(root)
        printBracket(root, "Finals")


def main():
    orderedSeeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
    divisions = ["East", "West", "South", "Midwest"]
    simulate(orderedSeeds, divisions)


if __name__ == "__main__":
    main()
