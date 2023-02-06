# Creating a grid world 5x5 to represent Example 3.5 from Reinforcment Learning An Introduction Second Edition
# by Richard S. Sutton and Andrew G. Barto

import numpy as np

np.set_printoptions(precision=2, suppress=True)

class Gridworld(object):
    # Setup new grid and place the agent in row 0, column 0
    def __init__(self):
        self.left_arrow = chr(0x2190)
        self.up_arrow = chr(0x2191)
        self.right_arrow = chr(0x2192)
        self.down_arrow = chr(0x2193)

        self.grid = np.zeros([5, 5], dtype=float)
        self.row = 0
        self.column = 0
        pass # End Method

    # Move the agent to a new grid if possible
    def move(self, row_delta, column_delta):
        reward = -1
        if self.row + row_delta < self.grid.shape[0] and self.row + row_delta >= 0:
            self.row += row_delta
            pass
        if self.column + column_delta < self.grid.shape[1] and self.column + column_delta >= 0:
            self.column += column_delta
        if (self.row, self.column) == (0, 1):
            (self.row, self.column) == (4, 1)
            reward = 10
            pass
        if (self.row, self.column) == (0, 3):
            (self.row, self.column) == (2, 3)
            reward = 5
            pass
        return reward
        pass # End Method

    # Display the current position
    def displayPosition(self):
        print(f'Position:\nrow: {self.row}\tcolumn: {self.column}')
        pass # End Method

    def displayGrid(self):
        print(self.grid)
        pass

    def display_block(self):
        block = np.chararray([3, 3], unicode=True)
        block.fill(chr(0x00B7))
        block[0, 1] = self.up_arrow
        block[1, 0] = self.left_arrow
        block[1, 2] = self.right_arrow
        block[2, 1] = self.down_arrow
        for r in range(block.shape[0]):
            for c in range(block.shape[1]):
                print(f' {block[r, c]}', end='')
                pass
            print()
            pass
        #print(block)
        pass

    pass # End Class Definition

# Test some of the functions
if __name__ == '__main__':
    grid_world = Gridworld()
    grid_world.displayPosition()
    grid_world.move(3, 4)
    grid_world.displayPosition()
    grid_world.displayGrid()
    grid_world.display_block()
    pass