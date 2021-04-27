from gameBike.keys import Key
import numpy as np


class BasicHeuristic:

    def __init__(self, speed=1, deterministic=True):

        self.speed = speed
        self.t_aux = -1
        self.deterministic = deterministic
        self.t = -1

    def request_view(self):
        return 6, True, True

    def __call__(self, view, t):
        if self.t < t:
            possible_moves = [Key.FORWARD, Key.TURN_LEFT, Key.TURN_RIGHT]
            aux = np.array([view[:6, 6], view[6, :6], view[7, :6]])
            filter_ = np.array([[3, 2, 1, 1, 1, 1], [3, 2, 1, 1, 1, 1],
                                [1, 1, 1, 1, 2, 3]])
            move = np.sum(aux + filter_, axis=1)
            self.t = t
            if self.deterministic:
                return possible_moves[np.argmin(move)], self.speed
            elif move[0] == move[1] == move[2]:
                return np.random.choice(possible_moves, p=[0.9, 0.05, 0.05]), self.speed
            else:
                return possible_moves[np.argmin(move)], self.speed
        return -1, -1

