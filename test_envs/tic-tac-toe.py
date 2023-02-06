import numpy as np

class GameBoard(object):
    
    def __init__(self):
        self.newBoard()
        pass
    def newBoard(self):
        self.board = np.array(
            [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
            )
        pass
    def placeMark(self, xo, row, column):
        if abs(row) < 3 and abs(column) < 3:
            if self.board[abs(row), abs(column)] == ' ':
                self.board[abs(row), abs(column)] = xo
            pass
        pass
    def printBoard(self):
        length = 15
        print(' ' + '_' * length + '_' + '_' * length + '_' + '_' * length + ' ')
        for row in range(3):
            print('|\t \t|\t \t|\t \t|')
            print('|\t \t|\t \t|\t \t|')
            for col in range(3):
                print(f'|\t{self.board[row, col]}\t', end='')
                pass
            print('|')
            print('|\t \t|\t \t|\t \t|')
            print('|' + '_' * length + '|' + '_' * length + '|' + '_' * length + '|')
            pass
        pass
    def checkVictory(self, xo):
        if (self.board[0, :] == xo).all():
            return True
        elif (self.board[1, :] == xo).all():
            return True
        elif (self.board[2, :] == xo).all():
            return True
        elif (self.board[:, 0] == xo).all():
            return True
        elif (self.board[:, 1] == xo).all():
            return True
        elif (self.board[:, 2] == xo).all():
            return True
        elif self.board[0, 0] == xo and self.board[1, 1] == xo and self.board[2, 2] == xo:
            return True
        elif self.board[0, 2] == xo and self.board[1, 1] == xo and self.board[2, 0] == xo:
            return True
        else:
            return False
        pass

game = GameBoard()
game.placeMark('x', 0, 2)
game.placeMark('x', 1, 2)
game.placeMark('x', 2, 2)
game.printBoard()
print(game.checkVictory('x'))