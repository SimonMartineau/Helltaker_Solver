"""
Grid Setup:
    E = Empty Space
    W = Wall
    B = Block
    S = Skeleton
    P = Player
    K = Key
    C = Chest
    G = Goal
"""


Level_1_HP = 23

Level_1_Grid = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'E', 'P', 'W', 'W'],
    ['W', 'W', 'E', 'E', 'S', 'E', 'E', 'W', 'W'],
    ['W', 'W', 'E', 'S', 'E', 'S', 'W', 'W', 'W'],
    ['W', 'E', 'E', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'E', 'B', 'E', 'E', 'B', 'E', 'W', 'W'],
    ['W', 'E', 'B', 'E', 'B', 'E', 'E', 'G', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
]

Level_9_HP = 32

Level_9_Grid = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'E', 'G', 'E', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'B', 'C', 'B', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'B', 'W', 'B', 'E', 'E', 'W', 'E', 'W', 'W'],
    ['W', 'B', 'E', 'E', 'B', 'B', 'B', 'E', 'E', 'K', 'W'],
    ['W', 'E', 'B', 'B', 'B', 'E', 'E', 'B', 'B', 'E', 'W'],
    ['W', 'W', 'P', 'E', 'B', 'E', 'E', 'B', 'E', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
]

