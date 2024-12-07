"""Contains the class Game for Ex 4.3-5 of OOP4Maths."""

import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
blinker = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Pattern:
    """The Pattern class represents a pattern in a Game."""

    def __init__(self, pattern):
        """Pattern class constructor method."""
        self.grid = pattern

    def flip_vertical(self):
        """Return new Pattern whose rows are in reversed order."""
        return Pattern(np.flipud(self.grid))

    def flip_horizontal(self):
        """Return Pattern whose columns are in reversed order."""
        return Pattern(np.flip(self.grid, 1))

    def flip_diag(self):
        """Return transpose of self."""
        return Pattern(np.matrix.transpose(self.grid))

    def rotate(self, n):
        """Return self rotated thru n right angles anticlock."""
        if n == 1:
            return Pattern(self.flip_horizontal().flip_diag().grid)
        elif n == 2:
            return Pattern(self.flip_horizontal().flip_diag()
                           .flip_horizontal().flip_diag().grid)    
        else:
            return Pattern(self.flip_horizontal().flip_diag()
            .flip_horizontal().flip_diag()
            .flip_horizontal().flip_diag().grid)
        


class Game:
    """The Game class reprents a circle."""

    def __init__(self, size):
        """Game class constructor method."""
        self.board = np.zeros((size, size))

    def play(self):
        """Start the game."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Move the game."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbour_count = convolve2d(self.board, stencil, mode='same')
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 \
                    if (neighbour_count[i, j] == 3
                        or (neighbour_count[i, j] == 2
                        and self.board[i, j])) else 0

    def __setitem__(self, key, value):
        """Set an item."""
        self.board[key] = value

    def show(self):
        """Show the game."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()
