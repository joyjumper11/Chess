import numpy as np
import pandas as pd

#8x8 array, dataframe will have columns and indices for algebraic notation
arrayBoard = np.zeros((8,8))

dfBoard = pd.DataFrame(arrayBoard,
                        columns = ["a", "b", "c", "d", "e", "f", "g", "h"],
                        index = ["8", "7", "6", "5", "4", "3", "2", "1"])




"""for i in dfBoard.columns:
    for j in dfBoard.index:
        if i == "a" or i == "c" or i == "e" or i == "g":
            if int(j) % 2 == 0:
                dfBoard[i][j] = 1.0
        else:
            if int(j) % 2 != 0:
                dfBoard[i][j] = 1.0
"""

#0 = black, 1 = white

#If we store everything as classes, we can iterate over the entire dataframe and call each object's valid moves function
#Then, based on each objects color, we can store those valid moves for each player as either w or b
    pass
class Rook:
    def __init__(self, color):
        self.color = color
        self.id = color + "R"

    def validMoves(self):
        pass

whiteRookOne = Rook("w")

dfBoard["a"]["1"] = whiteRookOne
print(dfBoard)
