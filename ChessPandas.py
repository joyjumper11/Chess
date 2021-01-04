import numpy as np
import pandas as pd

# global vars
columnLabels = ["A", "B", "C", "D", "E", "F", "G", "H"]
integerIndices = [8, 7, 6, 5, 4, 3, 2, 1]

def initBoard():
    #8x8 array, dataframe will have columns and indices for algebraic notation
    global columnLabels, integerIndices
    arrayBoard = np.zeros((8,8))
    dfBoard = pd.DataFrame(arrayBoard, columns = columnLabels, index = integerIndices)
    
    print(dfBoard)
    # TODO: populate board with pieces

    return dfBoard

# TODO: rewrite
def printBoard(dataFrame):

    # Board to print
    arrayBoard = np.zeros((8,8))
    dfPrint = pd.DataFrame(arrayBoard,
                            columns = columnLabels,
                            index = integerIndices)
    # Populate board
    for i in columnLabels:
        for j in integerIndices:
            if dataFrame[i][j] != 0 or dataFrame[i][j] != 0.0:
                dfPrint.loc[j,i] = dataFrame.loc[j,i].id
            else:
                dfPrint.loc[j,i] = "--"

    footer = dict(zip(columnLabels, columnLabels))
    dfPrint = dfPrint.append(footer, ignore_index = True)
    dfPrint.columns = [''] * len(dfPrint.columns)
    dfPrint.index = list(dfPrint.index[1:9]) + [""]

    print(dfPrint)
    pass



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
#Before every move, generate a list of all valid moves
#Then, check if the player's move is one of the valid options

class Rook:
    def __init__(self, color, position):
        self.color = color
        self.piece = "R"
        self.id = color + "R"
        self.pos = position #Store positions as a list where the first element is the column and the second element is the index ie ["A", 1]

    def validMoves(self):
        listOfValidMoves = []
        #For a rook, all possible valid moves are those that have the same column or index as the starting position
        #A valid move for a rook would consist of three parts: the piece id, the column to move to, and the index to move to
        #Therefore, a valid move has three elements: [self.id, "A", 5]

        #Get where you are in the list of columns and where you are in the list of indices

        currentIndex = 8 - self.pos[1]
        currentColumn = columnLabels.index(self.pos[0])
        
        #Now, start at whereAmIIndex and whereAmIColumn then increment/decrement, storing the moves that are to empty squares
        #Stop once you hit a square with a piece (check if it's opposite color, if it is store that move, otherwise don't)
        #Then, repeat for the other directions
        #For example, if at a4, you need to check a5, a6, a7, and a8, stopping if there is a piece in the way, inclusivity depends on what color that piece is
        #whereAmIColumn needs to be used four different times (4 directions to look at)
        #Therefore, store the value temporarily in a variable called i
        i = currentColumn
        print("heres", currentColumn, len(columnLabels))
        while i < len(columnLabels):
            print(i, "in loop")
            #Check to see if the square you are looking at is the piece you're already looking at
            if i == currentColumn:
                pass
            elif dfBoard[columnLabels[i]][currentIndex] == 0.0 or dfBoard[columnLabels[i]][currentIndex] == 0:
                listOfValidMoves.append([self.piece + self.pos[0], columnLabels[i], integerIndices[currentIndex]])
            else:
                print("HERE")
                #If the square isn't blank, it has a piece on it
                #That piece will belong to a class with the attribute color
                if dfBoard[columnLabels[i]][currentIndex].color == self.color:
                    break
                else:
                    print("here!!!!")
                    listOfValidMoves.append([self.piece + self.pos[0] + 'x', columnLabels[i], integerIndices[currentIndex]])
                    break
            i += 1
        """
        for i in range(len(columnLabels) - whereAmIColumn, len(columnLabels)):
            print(i)
            if dfBoard[columnLabels[i]][currentIndex] == 0.0 or dfBoard[columnLabels[i]][currentIndex] == 0:
                listOfValidMoves.append([self.piece, columnLabels[i], currentIndex])
            else:
                #If the square isn't blank, it has a piece on it
                #That piece will belong to a class with the attribute color
                if dfBoard[columnLabels[i]][currentIndex].color == self.color:
                    break
                else:
                    listOfValidMoves.append([self.piece, columnLabels[i], currentIndex])
                    break

        for i in integerIndices:
            #Checking if something is == to 0 won't work, have to check to see if the square is empty or is occupied by a piece of the opposite color
            if i != currentIndex and (dfBoard[currentColumn][i] == 0 or dfBoard[currentColumn][i] == 0.0):
                listOfValidMoves.append([self.piece, currentColumn, i])

        for j in columnLabels:
            if j != currentColumn and (dfBoard[j][currentIndex] == 0 or dfBoard[j][currentIndex]):
                listOfValidMoves.append([self.piece, j, currentIndex])
                """
        return listOfValidMoves

### TESTING ####
dfBoard = initBoard()

whiteRookOne = Rook("w", ["A", 1])
blackRookOne = Rook("b", ["D", 1])

#To avoid issue of changing panda slices (??), have to use .loc to change values, put index first and then the column
dfBoard.loc[1, "A"] = whiteRookOne

dfBoard.loc[1, "D"] = blackRookOne

printBoard(dfBoard)
print(whiteRookOne.validMoves())

#Before a move is made, set the previous square equal to 0
#Then, update the board with the new position and update the piece with its new position (if valid, that'll be added later)
# dfBoard.loc[whiteRookOne.position[1], whiteRookOne.position[0]] = 0
# whiteRookOne.position = ["E", 1]
# dfBoard.loc[1, "E"] = whiteRookOne
