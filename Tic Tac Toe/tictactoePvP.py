grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

def printBoard():
    print()
    print(" " + grid[0][0] + "|" + grid[0][1] + "|" + grid[0][2] + " ")
    print("-------")
    print(" " + grid[1][0] + "|" + grid[1][1] + "|" + grid[1][2] + " ")
    print("-------")
    print(" " + grid[2][0] + "|" + grid[2][1] + "|" + grid[2][2] + " ")
    
def clearGrid():
    for i in range(3):
        for j in range(3):
            grid[i][j] = ' '
    
playAgain = True
print()
print("*************************************** Welcome to Tic Tac Toe! ***************************************")
print("**************************** Player 1 will be 'X' and Player 2 will be 'O' ****************************")
print("************ To place your marker, just enter the row and column position from 1 to 3 each ************")
print("** Simply  enter the row number (1-3), press  enter, then  column number (1-3), and then press enter **")
print("****************************** Player 1 will start, let the game begin! *******************************")
print()
name1 = input("Player 1, enter your name: ")
name2 = input("Player 2, enter your name: ")
points1 = 0
points2 = 0
numTies = 0
playerTurn = 1
printBoard()
    
while (playAgain):
    currentPlayer = 1 if playerTurn % 2 != 0 else 2
    currentName = name1 if currentPlayer == 1 else name2
    print()
    row = int(input(currentName + ", enter your row number: "))
    column = int(input(currentName + ", enter your column number: "))
    rowIndex = row - 1
    columnIndex = column - 1
    grid[rowIndex][columnIndex] = 'X' if currentPlayer == 1 else 'O'
    printBoard()
    playerTurn += 1
    if (((grid[0][0]==grid[0][1])and(grid[0][1]==grid[0][2])and(grid[0][2]!=' '))or
        ((grid[1][0]==grid[1][1])and(grid[1][1]==grid[1][2])and(grid[1][2]!=' '))or
        ((grid[2][0]==grid[2][1])and(grid[2][1]==grid[2][2])and(grid[2][2]!=' '))or
        ((grid[0][0]==grid[1][0])and(grid[1][0]==grid[2][0])and(grid[2][0]!=' '))or
        ((grid[0][1]==grid[1][1])and(grid[1][1]==grid[2][1])and(grid[2][1]!=' '))or
        ((grid[0][2]==grid[1][2])and(grid[1][2]==grid[2][2])and(grid[2][2]!=' '))or
        ((grid[0][0]==grid[1][1])and(grid[1][1]==grid[2][2])and(grid[2][2]!=' '))or
        ((grid[0][2]==grid[1][1])and(grid[1][1]==grid[2][0])and(grid[2][0]!=' '))):

        if (currentPlayer == 1):
            points1 += 1
        else:
            points2 += 2
        print()
        print("Congrats " + currentName + " you won!")
        print(name1 + " has " + str(points1) + " and " + name2 + " has " + str(points2) + " points, while both players have tied " + str(numTies) + " times!")
        repeatAnswer = input("Play again? (y/n): ")
        playAgain = True if repeatAnswer == 'y' else False
        clearGrid()
        printBoard()
        playerTurn = 1
    elif (playerTurn == 10):
        numTies += 1
        print()
        print("Tie game!")
        print(name1 + " has " + str(points1) + " and " + name2 + " has " + str(points2) + " points, while both players have tied " + str(numTies) + " times!")
        repeatAnswer = input("Play again? (y/n): ")
        playAgain = True if repeatAnswer == 'y' else False
        clearGrid()
        printBoard()
        playerTurn = 1
        
    
    
    
    
    
