import re

# Sample Tic-Tac-Toe game
isGameOver = False
board = [[' - ', ' - ', ' - '], [' - ', ' - ', ' - '], [' - ', ' - ', ' - ']]


def printBoard():
    for i in board:
        for j in i:
            print(j, end="")
        print()
    print("************")


def updateBoard(row, column, value):
    board[row][column] = value


def parseInput(inputVal):
    input_array = inputVal.split(",")
    row = int(input_array[0][1])
    column = int(input_array[1][0])
    return {"row": row, "column": column}


def validateInput(input):
    regex = "\([012],[012]\)"
    return bool(re.match(regex, input))


def checkForWin():
    if (board[0][0] == board[0][1] == board[0][2] != ' - '
            or board[1][0] == board[1][1] == board[1][2] != ' - '
            or board[2][0] == board[2][1] == board[2][2] != ' - '
            or board[0][0] == board[1][1] == board[2][0] != ' - '
            or board[0][1] == board[1][1] == board[2][1] != ' - '
            or board[0][2] == board[1][2] == board[2][2] != ' - '
            or board[0][0] == board[1][1] == board[2][2] != ' - '
            or board[0][2] == board[1][1] == board[2][0] != ' - '):
        return True
    else:
        return False


def checkForDraw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' X ' or board[i][j] == ' O ':
                count = count + 1
    if count == 9:
        return True
    else:
        return False


# Main game starts here
while not isGameOver:
    printBoard()
    print("Player X turn")
    x = input("To which place you want to move(eg: (0,0), (1,2) etc:  ")

    isValidInput = validateInput(x)
    while not isValidInput:
        x = input("Input position is not valid please enter agian:  ")
        isValidInput = validateInput(x)

    positionMapOfX = parseInput(x)
    updateBoard(positionMapOfX["row"], positionMapOfX["column"], " X ")
    printBoard()
    if checkForWin():
        isGameOver = True
        print("Congrats, Plyaer X won the game")
        break
    if checkForDraw():
        isGameOver = True
        print("oops game is drawn")
        break

    print("Player O turn")
    o = input("To which place you want to move(eg: (0,0), (1,2) etc:  ")

    isValidInput = validateInput(o)
    while not isValidInput:
        o = input("Input position is not valid please enter agian:  ")
        isValidInput = validateInput(o)

    positionMapOfO = parseInput(o)
    updateBoard(positionMapOfO["row"], positionMapOfO["column"], " O ")
    printBoard()
    if checkForWin():
        isGameOver = True
        print("Congrats, Plyaer O won the game")
        break
    if checkForDraw():
        isGameOver = True
        print("oops game is drawn")
        break
