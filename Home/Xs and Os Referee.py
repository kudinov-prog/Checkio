"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns 
marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, 
vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. 
You are given a result of a game and you must determine if the game ends in a win or a draw 
as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
"""

from typing import List

def checkio(game_result: List[str]) -> str:
    new_list = []
    EMPTY = "."
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
                   
    x = 0
    y = 0
    for i in game_result:
        for z in i:
            new_list.append(z)
    for row in WAYS_TO_WIN:
        if new_list[row[0]] == new_list[row[1]] == new_list[row[2]]  and new_list[row[0]] != '.':
            return new_list[row[0]]        
            
    for i in new_list:
        if i == "X":
            x += 1
        elif i == "O":
            y += 1

    if x == y or x == 1 or y == 1:
        return "D"  
 
    if EMPTY not in new_list:
        return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")