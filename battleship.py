from typing import List
# Write any import statements here
"""
Returns the percentage possibility of hitting a ship on the board

    Args:
        R (int): The given amount of rows.
        C  (int): The given amount of columns.
        G (List): Spaces on the board
    Returns:
        int: the probability of getting a hit on the battleship board.
"""

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    total_cells = R * C
    battleships = sum(sum(row) for row in G)
    return battleships / total_cells

R = 4
C = 5
G = [[0, 1, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1]]
print(getHitProbability(R, C, G)) 
