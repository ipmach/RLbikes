from scipy.sparse import csr_matrix
from board_game import TableGame
from keys import Key
import numpy as np


class Game(TableGame):

    def get_view(self, coord, range_):
        """
        Obtain correct window of view plus corrections
        :param coord: coordinates bike
        :param range_: range of the view per size from the bike
        :return: view, (corrections)
        """

        if coord[0] - range_ >= 0:  # Check if x is close to a low border
            low_x = coord[0] - range_
            low_x_correction = 0
        else:
            low_x = 0
            low_x_correction = abs(coord[0] - range_)

        if coord[1] - range_ >= 0:  # Check if y is close to a low border
            low_y = coord[1] - range_
            low_y_correction = 0
        else:
            low_y = 0
            low_y_correction = abs(coord[1] - range_)

        if coord[0] + range_ + 1 < self.board.shape[0]:  # Check if x is close to a high border
            high_x = coord[0] + range_ + 1
            high_x_correction = 2 * range_ + 1
        else:
            high_x = self.board.shape[0]
            high_x_correction = (2 * range_ + 1) - ((coord[0] + range_ + 1) - self.board.shape[0])

        if coord[1] + range_ + 1 < self.board.shape[1]:  # Check if y is close to a high border
            high_y = coord[1] + range_ + 1
            high_y_correction = 2 * range_ + 1
        else:
            high_y = self.board.shape[1]
            high_y_correction = (2 * range_ + 1) - ((coord[1] + range_ + 1) - self.board.shape[1])

        # Create view
        view = self.board[low_x: high_x, low_y: high_y]

        return view, (low_x_correction, low_y_correction,
                      high_x_correction, high_y_correction)

    def get_view_bike(self, bike, range_, mono=False, rotate=False):
        """
        Get view of the bike
        :param bike: number bike
        :param range_: range of view
        :param mono: binary image or not
        :param rotate: rotate the view so the bike is always looking same position
        :return: the view of the bike
        """
        coord = self.bikes[bike]

        # Obtain view
        view, correction = self.get_view(coord, range_)

        # Apply corrections
        view_aux = np.ones((2 * range_ + 1, 2 * range_ + 1))
        view_aux[correction[0]:correction[2], correction[1]:correction[3]] = view
        view = view_aux

        if mono:  # make a binary view floor 0 rest 1
            reduce = np.vectorize(lambda x: x if x < 1 else 1)
            view = reduce(view)

        if rotate:  # rotate the image so the bike is always looking the same place
            if self.bikes_orientation[bike] == Key.RIGHT:
                view = np.rot90(view, k=1)
            elif self.bikes_orientation[bike] == Key.LEFT:
                view = np.rot90(view, k=3)
            elif self.bikes_orientation[bike] == Key.UP:
                view = np.rot90(view, k=2)
        return view

    def get_view_board(self, only_update=False, compress=False):
        """
        Get view of the board game
        :param only_update: only show update pixels
        :param compress: compress the view
        :return: the board view
        """
        board = np.copy(self.board)
        reduce = np.vectorize(lambda x: x if x < 1 else 1)

        if only_update:  # Only show the last update pixels
            index = np.nonzero(reduce(board) - reduce(self.old_board))
            board = np.zeros(board.shape)
            board[index] = self.board[index]

        if compress:  # Compress the board in a sparse matrix
            board = csr_matrix(board)

        return board