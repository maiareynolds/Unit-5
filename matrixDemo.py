#Maia Reynolds
#4/26/18
#matrixDemo.py - lists in lists

def printBoard(board):
    for r in range(0,3):
        for c in range(0,3):
            print(board[r][c],end=" ")
        print()

board=[["a","b","c"],["d","e","f"],["g","h","i"]]

printBoard(board)