from keys import Key
import numpy as np


class BasicHeuristic:

    def __call__(self, view):
        possible_moves = [Key.FORWARD, Key.TURN_LEFT, Key.TURN_RIGHT]
        aux = np.array([view[:3, 3], view[3, :3], view[4, :3]])
        filter_ = np.array([[1, 2, 3], [3, 2, 1], [1, 2, 3]])
        move = np.sum(aux + filter_, axis=1)
        return possible_moves[np.argmin(move)]