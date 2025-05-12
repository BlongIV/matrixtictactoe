import random

def inarow_Neast(ch, r_start, c_start, A, N):          # the in a row functions are used from previous HWs
    """This function checks if there are N of the same
    elemetn ch in a row to the east.
    """
    height = len(A)
    width = len(A[0])
    if c_start + (N-1) > width - 1:
        return False
    elif r_start < 0 or r_start > height - 1:
        return False
    elif c_start < 0 or c_start > width - 1:
        return False
    elif A[r_start][c_start] != ch:
        return False
    
    for i in range(1, N):
        if A[r_start][c_start + i] != ch:
            return False
    return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """This function checks if there are N of the same
    elemetn ch in a row to the south.
    """
    height = len(A)
    width = len(A[0])
    if r_start + (N-1) > height - 1:
        return False
    elif r_start < 0 or r_start > height - 1:
        return False
    elif c_start < 0 or c_start > width - 1:
        return False
    elif A[r_start][c_start] != ch:
        return False
    
    for i in range(1, N):
        if A[r_start + i][c_start] != ch:
            return False
    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """This function checks if there are N of the same
    elemetn ch in a row to the southeast.
    """
    height = len(A)
    width = len(A[0])
    if r_start + (N-1) > height - 1 or c_start + (N-1) > width - 1:
        return False
    elif r_start < 0 or r_start > height - 1:
        return False
    elif c_start < 0 or c_start > width - 1:
        return False
    elif A[r_start][c_start] != ch:
        return False
    
    for i in range(1, N):
        if A[r_start + i][c_start + i] != ch:
            return False
    return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """This function checks if there are N of the same
    elemetn ch in a row to the northeast.
    """
    height = len(A)
    width = len(A[0])
    if c_start + (N-1) > width - 1 or r_start - (N-1) < 0:
        return False
    elif r_start < 0 or r_start > height - 1:
        return False
    elif c_start < 0 or c_start > width - 1:
        return False
    elif A[r_start][c_start] != ch:
        return False
    
    for i in range(1, N):
        if A[r_start - i][c_start + i] != ch:
            return False
    return True


class smallBoard:            # The smallBoard class is used to store the information in the 9 small boards
    def __init__(self):
        """This initialize a standard tic tac toe board
        """
        self.data = [[' ' for col in range(3)] for row in range(3)]
    
    def __repr__(self):
        """ Creates a visual representation of the tic tac toe board
        """
        s = ''
        s += ' ' + self.data[0][0] + ' | ' + self.data[0][1] + ' | ' + self.data[0][2]
        s += '\n'
        s += '---|---|---'
        s += '\n'
        s += ' ' + self.data[1][0] + ' | ' + self.data[1][1] + ' | ' + self.data[1][2]
        s += '\n'
        s += '---|---|---'
        s += '\n'
        s += ' ' + self.data[2][0] + ' | ' + self.data[2][1] + ' | ' + self.data[2][2]
        return s

    def addMove(self, row, col, ox):
        """ This method adds a specified move to a given row and column
        """
        if self.data[row][col] == ' ':
            self.data[row][col] = ox

    def delMove(self, row, col):
        """ This method deletes any move made in a given row and column
        """
        self.data[row][col] = ' '
        
    def checkWins(self, ox):
        """ This method checks for a win for a specified character on a tic tac toe board
        """
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if inarow_Neast(ox, row, col, self.data, 3) == True:
                    return True
                if inarow_Nsouth(ox, row, col, self.data, 3) == True:
                    return True
                if inarow_Nnortheast(ox ,row, col, self.data, 3) == True:
                    return True
                if inarow_Nsoutheast(ox, row, col, self.data, 3) == True:
                    return True
        return False
    
    def addWin(self, ox):
        """ This method changes the characters of a small tic tac toe board to signify a win.
        It first deletes all previous moves, then depending on which character won, replaces all squares
        with the lowercase of that character.
        """
        for row in range(3):
            for col in range(3):
                self.delMove(row, col)
        if ox == 'X':
            for row in range(3):
                for col in range(3):
                    self.addMove(row, col, 'x')
        if ox == 'O':
            for row in range(3):
                for col in range(3):
                    self.addMove(row, col, 'o')

    def checkFullBoard(self):
        for row in range(3):
            for col in range(3):
                if self.data[row][col] == ' ':
                    return False
        return True



    
class bigBoard:          # The bigBoard class is used to store infomation of 9 smallBoards and has all methods needed to play matrix tic tac toe
    def __init__(self):
        """ This method creates a large tic tac toe board out of smallBoards
        """
        self.data = [[smallBoard() for col in range(3)] for row in range(3)]
    
    def __repr__(self):
        """ This method provides a visual representation of the large tic tac toe board with the smaller boards in it
        """
        s = ''
        s += ' ' + self.data[0][0].data[0][0] + ' | ' + self.data[0][0].data[0][1] + ' | ' + self.data[0][0].data[0][2] + '  ||  ' + self.data[0][1].data[0][0] + ' | ' + self.data[0][1].data[0][1] + ' | ' + self.data[0][1].data[0][2] + '  ||  ' + self.data[0][2].data[0][0] + ' | ' + self.data[0][2].data[0][1] + ' | ' + self.data[0][2].data[0][2] + ' '
        s += '\n'
        s += '---|---|--- || ---|---|--- || ---|---|---'
        s += '\n'
        s += ' ' + self.data[0][0].data[1][0] + ' | ' + self.data[0][0].data[1][1] + ' | ' + self.data[0][0].data[1][2] + '  ||  ' + self.data[0][1].data[1][0] + ' | ' + self.data[0][1].data[1][1] + ' | ' + self.data[0][1].data[1][2] + '  ||  ' + self.data[0][2].data[1][0] + ' | ' + self.data[0][2].data[1][1] + ' | ' + self.data[0][2].data[1][2] + ' '
        s += '\n'
        s += '---|---|--- || ---|---|--- || ---|---|---'
        s += '\n'
        s += ' ' + self.data[0][0].data[2][0] + ' | ' + self.data[0][0].data[2][1] + ' | ' + self.data[0][0].data[2][2] + '  ||  ' + self.data[0][1].data[2][0] + ' | ' + self.data[0][1].data[2][1] + ' | ' + self.data[0][1].data[2][2] + '  ||  ' + self.data[0][2].data[2][0] + ' | ' + self.data[0][2].data[2][1] + ' | ' + self.data[0][2].data[2][2] + ' '
        s += '\n'
        s += '============||=============||============'
        s += '\n'
        s += ' ' + self.data[1][0].data[0][0] + ' | ' + self.data[1][0].data[0][1] + ' | ' + self.data[1][0].data[0][2] + '  ||  ' + self.data[1][1].data[0][0] + ' | ' + self.data[1][1].data[0][1] + ' | ' + self.data[1][1].data[0][2] + '  ||  ' + self.data[1][2].data[0][0] + ' | ' + self.data[1][2].data[0][1] + ' | ' + self.data[1][2].data[0][2] + ' '
        s += '\n'
        s += '---|---|--- || ---|---|--- || ---|---|---'
        s += '\n'
        s += ' ' + self.data[1][0].data[1][0] + ' | ' + self.data[1][0].data[1][1] + ' | ' + self.data[1][0].data[1][2] + '  ||  ' + self.data[1][1].data[1][0] + ' | ' + self.data[1][1].data[1][1] + ' | ' + self.data[1][1].data[1][2] + '  ||  ' + self.data[1][2].data[1][0] + ' | ' + self.data[1][2].data[1][1] + ' | ' + self.data[1][2].data[1][2] + ' '
        s += '\n'
        s += '---|---|--- || ---|---|--- || ---|---|---'
        s += '\n'
        s += ' ' + self.data[1][0].data[2][0] + ' | ' + self.data[1][0].data[2][1] + ' | ' + self.data[1][0].data[2][2] + '  ||  ' + self.data[1][1].data[2][0] + ' | ' + self.data[1][1].data[2][1] + ' | ' + self.data[1][1].data[2][2] + '  ||  ' + self.data[1][2].data[2][0] + ' | ' + self.data[1][2].data[2][1] + ' | ' + self.data[1][2].data[2][2] + ' '
        s += '\n'
        s += '============||=============||============'
        s += '\n'
        s += ' ' + self.data[2][0].data[0][0] + ' | ' + self.data[2][0].data[0][1] + ' | ' + self.data[2][0].data[0][2] + '  ||  ' + self.data[2][1].data[0][0] + ' | ' + self.data[2][1].data[0][1] + ' | ' + self.data[2][1].data[0][2] + '  ||  ' + self.data[2][2].data[0][0] + ' | ' + self.data[2][2].data[0][1] + ' | ' + self.data[2][2].data[0][2] + ' '
        s += '\n'
        s += '---|---|--- || ---|---|--- || ---|---|---'
        s += '\n'
        s += ' ' + self.data[2][0].data[1][0] + ' | ' + self.data[2][0].data[1][1] + ' | ' + self.data[2][0].data[1][2] + '  ||  ' + self.data[2][1].data[1][0] + ' | ' + self.data[2][1].data[1][1] + ' | ' + self.data[2][1].data[1][2] + '  ||  ' + self.data[2][2].data[1][0] + ' | ' + self.data[2][2].data[1][1] + ' | ' + self.data[2][2].data[1][2] + ' '
        s += '\n'
        s += '---|---|--- || ---|---|--- || ---|---|---'
        s += '\n'
        s += ' ' + self.data[2][0].data[2][0] + ' | ' + self.data[2][0].data[2][1] + ' | ' + self.data[2][0].data[2][2] + '  ||  ' + self.data[2][1].data[2][0] + ' | ' + self.data[2][1].data[2][1] + ' | ' + self.data[2][1].data[2][2] + '  ||  ' + self.data[2][2].data[2][0] + ' | ' + self.data[2][2].data[2][1] + ' | ' + self.data[2][2].data[2][2] + ' '
        s += '\n'
        
        return s
    

    def addBigMove(self, bigRow, bigCol, lilRow, lilCol, ox):
        """ This method adds a move for a specified character to a specific square of a specific smallBoard in the larger tic tac toe board
        """
        if self.data[bigRow][bigCol].data[lilRow][lilCol] == ' ':
            self.data[bigRow][bigCol].addMove(lilRow, lilCol, ox)
    
    def checkSmallWin(self, bigRow, bigCol, ox):
        """ This method checks if a specified small board has been won by a specific character
        """
        if self.data[bigRow][bigCol].checkWins(ox) == True:
            self.data[bigRow][bigCol].addWin(ox)

    def nextBoard(self, prevRow, prevCol):
        """ This method uses the index of the previous player's move to return the index of the next player's move.
        """
        nextRow = prevRow
        nextCol = prevCol
        while self.data[nextRow][nextCol].data[0][0] == 'x' or self.data[nextRow][nextCol].data[0][0] == 'o':    # this method applies the rules of the game on where a move sends the next player
            nextCol += 1
            if nextCol > 2:
                nextCol = 0
                nextRow += 1
                if nextRow > 2:
                    nextRow = 0
                    nextCol = 0
        
        return nextRow, nextCol
    
    def checkSmallBoardWin(self, bigRow, bigCol, ox):
        """ This method checks if a specific smallBoard has been won by a specified character. Returns True or False
        """
        if ox == 'X':
            if self.data[bigRow][bigCol].data[0][0] == 'x':
                return True
            else:
                return False
        if ox == 'O':
            if self.data[bigRow][bigCol].data[0][0] == 'o':
                return True
            else:
                return False
            
    def checkBigWinEast(self, row, col, ox):                   # the following four methods are altered versions of the check n in a row functions
        """ Checks if there are 3 boards won by a specified character to the East
        """
        if col + 2 > 2:
            return False
        elif row < 0 or row > 2:
            return False
        elif col < 0 or col > 2:
            return False
        if ox == 'X':
            if self.data[row][col].data[0][0] != 'x':
                return False
        elif ox == 'O':
            if self.data[row][col].data[0][0] != 'o':
                return False
            
        for i in range(1, 3):
            if ox == 'X':
                if self.data[row][col + i].data[0][0] != 'x':
                    return False
            if ox == 'O':
                if self.data[row][col + i].data[0][0] != 'o':
                    return False
        return True
    
    def checkBigWinSouth(self, row, col, ox):
        """ Checks if there are 3 boards won by a specified character to the South
        """
        if row + 2 > 2:
            return False
        elif row < 0 or row > 2:
            return False
        elif col < 0 or col > 2:
            return False
        if ox == 'X':
            if self.data[row][col].data[0][0] != 'x':
                return False
        elif ox == 'O':
            if self.data[row][col].data[0][0] != 'o':
                return False
            
        for i in range(1, 3):
            if ox == 'X':
                if self.data[row + i][col].data[0][0] != 'x':
                    return False
            if ox == 'O':
                if self.data[row + i][col].data[0][0] != 'o':
                    return False
        return True
    
    def checkBigWinNortheast(self, row, col, ox):
        """ Checks if there are 3 boards won by a specified character to the Northeast
        """
        if col + 2 > 2:
            return False
        elif row - 2 < 0:
            return False
        elif row < 0 or row > 2:
            return False
        elif col < 0 or col > 2:
            return False
        if ox == 'X':
            if self.data[row][col].data[0][0] != 'x':
                return False
        elif ox == 'O':
            if self.data[row][col].data[0][0] != 'o':
                return False
            
        for i in range(1, 3):
            if ox == 'X':
                if self.data[row - i][col + i].data[0][0] != 'x':
                    return False
            if ox == 'O':
                if self.data[row - i][col + i].data[0][0] != 'o':
                    return False
        return True
    
    def checkBigWinSoutheast(self, row, col, ox):
        """ Checks if there are 3 boards won by a specified character to the Southeast
        """
        if col + 2 > 2:
            return False
        elif row + 2 > 2:
            return False
        elif row < 0 or row > 2:
            return False
        elif col < 0 or col > 2:
            return False
        if ox == 'X':
            if self.data[row][col].data[0][0] != 'x':
                return False
        elif ox == 'O':
            if self.data[row][col].data[0][0] != 'o':
                return False
            
        for i in range(1, 3):
            if ox == 'X':
                if self.data[row + i][col + i].data[0][0] != 'x':
                    return False
            if ox == 'O':
                if self.data[row + i][col + i].data[0][0] != 'o':
                    return False
        return True
    
    
    def checkBigBoardWin(self, ox):
        """ This method checks if the specified character has won the bigBoard
        """
        for row in range(3):
            for col in range(3):
                if self.checkBigWinEast(row, col, ox) == True:
                    return True
                elif self.checkBigWinSouth(row, col, ox) == True:
                    return True
                elif self.checkBigWinNortheast(row, col, ox) == True:
                    return True
                elif self.checkBigWinSoutheast(row, col, ox) == True:
                    return True
        return False
    
    def checkFullBigBoard(self):
        for row in range(3):
            for col in range(3):
                if self.data[row][col].checkFullBoard() == False:
                    return False
        return True
    
    def playTwoPlayer(self):
        """ This method plays out a complete two player game of matrix tic tac toe.
        """
        valid_indecies = ['0','1','2'] # this is the list of valid user inputs
        print("Welcome to Matrix Tic Tac Toe!")
        print()
        print("Player O will go first.")
        print()
        print("Player O, choose what board you would like to make your first move on.")
        print("Boards are indexed from 0 and row comes before column. So, the middle board is row 1 column 1.")
        print()
        print(self)
        print()
        
        while True:         # These while True loops used for inputs make sure that the user enters one of the desired inputs
            ORow = input("Choose your starting row: ")
            if ORow in valid_indecies:
                ORow = int(ORow)
                break
            else:
                print("Invalid Choice. Please choose a valid index.")
        while True:
            OColumn = input("Choose your starting column: ")
            if OColumn in valid_indecies:
                OColumn = int(OColumn)
                break
            else:
                print("Invalid Choice. Please choose a valid index.")
        
        print()
        print("Choose which square you want on the smaller board you chose.")
        print("The smaller boards are indexed just like the larger ones.")
        while True:
            print()
            print(f"Player O will make their next move in the board in row {ORow} and in column {OColumn}")
            print()
            while True:
                oRow = input("Choose what row you want: ")
                if oRow in valid_indecies:
                    oRow = int(oRow)
                    break
                else:
                    print("Invalid Choice. Please choose a valid index.")
            while True:
                oCol = input("Choose what column you want: ")
                if oCol in valid_indecies:
                    oCol = int(oCol)
                    break
                else:
                    print("Invalid Choice. Please choose a valid index.")
            
            self.addBigMove(ORow, OColumn, oRow, oCol, 'O')
            print()
            self.checkSmallWin(ORow, OColumn, 'O')
            print(self)
            if self.checkBigBoardWin('O') == True:
                print()
                print("Player O wins! Congratulations!")
                break
            if self.checkFullBigBoard() == True:
                print()
                print("Board is full. There is no winner")
                break
            XRow, XColumn = self.nextBoard(oRow, oCol)
            print()
            print(f"Player X will make their next move in the board in row {XRow} and in column {XColumn}")
            print()
            while True:
                xRow = input("Choose what row you want: ")
                if xRow in valid_indecies:
                    xRow = int(xRow)
                    break
                else:
                    print("Invalid Choice. Please choose a valid index.")
            while True:
                xCol = input("Choose what column you want: ")
                if xCol in valid_indecies:
                    xCol = int(xCol)
                    break
                else:
                    print("Invalid Choice. Please choose a valid index.")
            self.addBigMove(XRow, XColumn, xRow, xCol, 'X')
            print()
            self.checkSmallWin(XRow, XColumn, 'X')
            print(self)
            if self.checkBigBoardWin('X') == True:
                print()
                print("Player X wins! Congratulations!")
                break
            if self.checkFullBigBoard() == True:
                print()
                print("Board is full. There is no winner")
                break
            ORow, OColumn = self.nextBoard(xRow, xCol)
    
    def findWins(self, Row, Col, ox):
        """ This method finds all the potential wins for x or o on a specified smallBoard
        """
        wins = []
        for row in range(3):
            for col in range(3):
                if self.data[Row][Col].data[row][col] == ' ':
                    self.addBigMove(Row, Col, row, col, ox)
                    if self.data[Row][Col].checkWins(ox) == True:
                        wins.append([row, col])
                    self.data[Row][Col].delMove(row, col)
        return wins

    
    def aiMove(self, Row, Col, ox):
        """ This method finds the move for the AI on a given board. If the AI has a clear win, it will play that move at first priority.
        If the opponent has a clear win, the AI will block that move. If neither of the first two conditions are true, the AI will play its
        move in a random square on the board.
        """
        if ox == 'X':
            ownWins = self.findWins(Row, Col, 'X')
            oppWins = self.findWins(Row, Col, 'O')
            if len(ownWins) >= 1:
                return ownWins[0][0], ownWins[0][1]
            elif len(oppWins) >= 1:
                return oppWins[0][0], oppWins[0][1]
            else:
                while True:
                    row = random.choice([0,1,2])
                    col = random.choice([0,1,2])
                    if self.data[Row][Col].data[row][col] == ' ':
                        return row, col
        if ox == 'O':
            ownWins = self.findWins(Row, Col, 'O')
            oppWins = self.findWins(Row, Col, 'X')
            if len(ownWins) >= 1:
                return ownWins[0][0], ownWins[0][1]
            elif len(oppWins) >= 1:
                return oppWins[0][0], oppWins[0][1]
            else:
                while True:
                    row = random.choice([0,1,2])
                    col = random.choice([0,1,2])
                    if self.data[Row][Col].data[row][col] == ' ':
                        return row, col
    
    def playVSai(self, ox):
        """ This method allows for a player to play a full game of matrix tic tac toe vs AI. The player 
        can play as either X or O.
        """
        valid_indecies = ['0','1','2']
        if ox == 'X':
            print("Welcome to Matrix Tic Tac Toe!")
            print()
            print("You are playing as Player X.")
            print("Player O will go first.")
            print()
            print("Player O, will choose the starting board.")
            print("Boards are indexed from 0 and row comes before column. So, the middle board is row 1 column 1.")
            print()
            print(self)
            print()
            ORow = random.choice([0,1,2])
            OColumn = random.choice([0,1,2])
            print()
            print("Choose which square you want on the smaller board you chose.")
            print("The smaller boards are indexed just like the larger ones.")
            while True:
                print()
                print(f"Player O will make their next move in the board in row {ORow} and in column {OColumn}")
                print()
                oRow, oCol = self.aiMove(ORow, OColumn, 'O')
                self.addBigMove(ORow, OColumn, oRow, oCol, 'O')
                print()
                self.checkSmallWin(ORow, OColumn, 'O')
                print(self)
                if self.checkBigBoardWin('O') == True:
                    print()
                    print("Player O wins! Congratulations!")
                    break
                if self.checkFullBigBoard() == True:
                    print()
                    print("Board is full. There is no winner")
                    break
                XRow, XColumn = self.nextBoard(oRow, oCol)
                print()
                print(f"Player X will make their next move in the board in row {XRow} and in column {XColumn}")
                print()
                while True:
                    xRow = input("Choose what row you want: ")
                    if xRow in valid_indecies:
                        xRow = int(xRow)
                        break
                    else:
                        print("Invalid Choice. Please choose a valid index.")
                while True:
                    xCol = input("Choose what column you want: ")
                    if xCol in valid_indecies:
                        xCol = int(xCol)
                        break
                    else:
                        print("Invalid Choice. Please choose a valid index.")

                self.addBigMove(XRow, XColumn, xRow, xCol, 'X')
                print()
                self.checkSmallWin(XRow, XColumn, 'X')
                print(self)
                if self.checkBigBoardWin('X') == True:
                    print()
                    print("Player X wins! Congratulations!")
                    break
                if self.checkFullBigBoard() == True:
                    print()
                    print("Board is full. There is no winner")
                    break
                ORow, OColumn = self.nextBoard(xRow, xCol)


        if ox == 'O':
            print("Welcome to Matrix Tic Tac Toe!")
            print()
            print("You are playing as player O.")
            print("Player O will go first.")
            print()
            print("Player O, choose what board you would like to make your first move on.")
            print("Boards are indexed from 0 and row comes before column. So, the middle board is row 1 column 1.")
            print()
            print(self)
            print()
            while True:
                ORow = input("Choose your starting row: ")
                if ORow in valid_indecies:
                    ORow = int(ORow)
                    break
                else:
                    print("Invalid Choice. Please choose a valid index.")
            while True:
                OColumn = input("Choose your starting column: ")
                if OColumn in valid_indecies:
                    OColumn = int(OColumn)
                    break
                else:
                    print("Invalid Choice. Please choose a valid index.")

            print()
            print("Choose which square you want on the smaller board you chose.")
            print("The smaller boards are indexed just like the larger ones.")
            while True:
                print()
                print(f"Player O will make their next move in the board in row {ORow} and in column {OColumn}")
                print()
                while True:
                    oRow = input("Choose what row you want: ")
                    if oRow in valid_indecies:
                        oRow = int(oRow)
                        break
                    else:
                        print("Invalid Choice. Please choose a valid index.")
                while True:
                    oCol = input("Choose what column you want: ")
                    if oCol in valid_indecies:
                        oCol = int(oCol)
                        break
                    else:
                        print("Invalid Choice. Please choose a valid index.")
                        
                self.addBigMove(ORow, OColumn, oRow, oCol, 'O')
                print()
                self.checkSmallWin(ORow, OColumn, 'O')
                print(self)
                if self.checkBigBoardWin('O') == True:
                    print()
                    print("Player O wins! Congratulations!")
                    break
                if self.checkFullBigBoard() == True:
                    print()
                    print("Board is full. There is no winner")
                    break
                XRow, XColumn = self.nextBoard(oRow, oCol)
                print()
                print(f"Player X will make their next move in the board in row {XRow} and in column {XColumn}")
                print()
                xRow, xCol = self.aiMove(XRow, XColumn, 'X')
                
                self.addBigMove(XRow, XColumn, xRow, xCol, 'X')
                print()
                self.checkSmallWin(XRow, XColumn, 'X')
                print(self)
                if self.checkBigBoardWin('X') == True:
                    print()
                    print("Player X wins! Congratulations!")
                    break
                if self.checkFullBigBoard() == True:
                    print()
                    print("Board is full. There is no winner")
                    break
                ORow, OColumn = self.nextBoard(xRow, xCol)

    def playAIvsAI(self):
        """ This method for bigBoard plays a game with AI vs AI. It only prints the final board and the winner, if any 
        """
        ORow = random.choice([0,1,2])
        OColumn = random.choice([0,1,2])
        while True:
            oRow, oCol = self.aiMove(ORow, OColumn, 'O')
            self.addBigMove(ORow, OColumn, oRow, oCol, 'O')
            self.checkSmallWin(ORow, OColumn, 'O')
            if self.checkBigBoardWin('O') == True:
                print()
                print(self)
                print()
                print("Player O wins! Congratulations!")
                break
            if self.checkFullBigBoard() == True:
                print()
                print(self)
                print()
                print("Board is full. There is no winner")
                break
            XRow, XColumn = self.nextBoard(oRow, oCol)
            xRow, xCol = self.aiMove(XRow, XColumn, 'X')
            self.addBigMove(XRow, XColumn, xRow, xCol, 'X')
            self.checkSmallWin(XRow, XColumn, 'X')
            if self.checkBigBoardWin('X') == True:
                print()
                print(self)
                print()
                print("Player X wins! Congratulations!")
                break
            if self.checkFullBigBoard() == True:
                print()
                print(self)
                print()
                print("Board is full. There is no winner")
                break
            ORow, OColumn = self.nextBoard(xRow, xCol)




def playGame():  # this function is how the user can choose to play all gamemodes
    """ This function plays out a full game of matrix tic tac toe of the user's choosing.
    The user can choose to play either a 1 or 2 player game. Either against the AI or 
    against another person.
    """
    while True:
        b = bigBoard()
        valid_player_nums = ['0','1','2']
        valid_players = ['X', 'O']
        print()
        print("Would you like to play 0 player (computer vs computer), 1 player (against the computer), or 2 player (against another human)?")
        while True:
            players = input("Please choose 0 player, 1 player, or 2 player (type 0 or 1 or 2): ")
            if players in valid_player_nums:
                players = int(players)
                break
            else:
                print("Invalid choice. Please enter either 0 or 1 or 2.")
        if players == 0:
            b.playAIvsAI()
        if players == 2:
            b.playTwoPlayer()
        if players == 1:
            print()
            print("Would you like to play as Player X or Player O?")
            while True:
                XorO = input("Please choose X or O (type X or O): ")
                if XorO in valid_players:
                    break
                else:
                    print("Invalid choice. Please choose X or O.")
            if XorO == 'X':
                b.playVSai('X')
            elif XorO == 'O':
                b.playVSai('O')
        print()
        while True:
            quitORnot = input("Would you like to quit? (type y or n): ")
            if quitORnot in ['y', 'n']:
                break
            else:
                print("Invalid choice. Please only choose from y or n.")
        if quitORnot == 'y':
            return
        else:
            continue

