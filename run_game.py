import matplotlib.pyplot as plt
from game import Game
import numpy as np
import time


class RunGame:

    def __init__(self, game_, time_=0.1, view=True):
        """
        Run game in real time
        :param game_: game we want to run
        :param time_: time between each game update
        :param view: True if we want to see the game in pyplot
        """
        self.game = game_
        self.time_ = time_
        self.view = view
        self.moves = None
        self.t = 0

    def get_moves(self):
        """
        Return the moves pointers
        :return: moves
        """
        return self.moves

    def get_t(self):
        """
        Return time step
        :return: time step
        """
        return self.t

    def view_plt(self):
        plt.imshow(self.game.get_view_board())
        plt.title('time t = {}'.format(self.t))
        plt.pause(self.time_)
        plt.clf()
        
    def __call__(self):
        """
        Start the game, will run until the game raise the over flag
        :return:
        """
        while not self.game.is_over():  # Game loop
            self.moves = self.game.new_move()  # Initialize new move
            if self.view:  # with visualization
                self.view_plt()
            else:  # Without visualization
                time.sleep(self.time_)
            self.game.apply_round(self.moves)  # Apply move
            self.t += 1

        print('Bike {} won in t={}!!!'.format(np.argmax(self.game.alive.reshape(-1)),
                                              self.t))




