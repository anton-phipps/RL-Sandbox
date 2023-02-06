# Creating a grid world 5x5 to represent Example 3.5 from Reinforcment Learning An Introduction Second Edition
# by Richard S. Sutton and Andrew G. Barto

import numpy as np

class Gridworld(object):
    # Setup new grid and place the agent in row 0, column 0
    def __init__(self):
        self.grid = np.zeros([5, 5], dtype=float)
        self.row = 0
        self.column = 0
        pass # End Method

    # Move the agent to a new grid if possible
    def move(self, row_delta, column_delta):
        if self.row + row_delta < self.grid.shape[0] and self.row + row_delta >= 0:
            self.row += row_delta
            pass
        if self.column + column_delta < self.grid.shape[1] and self.column + column_delta >= 0:
            self.column += column_delta
        pass # End Method

    # Display the current position
    def displayPosition(self):
        print(f'Position:\nrow: {self.row}\tcolumn: {self.column}')
        pass # End Method

    pass # End Class Definition


if __name__ == '__main__':
    grid_world = Gridworld()
    grid_world.move(3, 4)
    grid_world.displayPosition()
    grid_world.move(-1, -6)
    grid_world.displayPosition()
    grid_world.move(5, 1)
    grid_world.displayPosition()