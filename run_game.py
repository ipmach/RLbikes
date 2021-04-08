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
        
    def __call__(self):
        """
        Start the game, will run until the game raise the over flag
        :return:
        """
        while not self.game.is_over():  # Game loop
            moves = self.game.new_move()  # Initialize new move
            if self.view:  # with visualization
                plt.imshow(self.game.get_view_board())
                plt.pause(self.time_)
                plt.clf()
            else:  # Without visualization
                time.sleep(self.time_)
            self.game.apply_round(moves)  # Apply move

        print('Bike {} won!!!'.format(np.argmax(self.game.alive.reshape(-1))))


game = Game(load_map='maps/map_1.npy')
a = RunGame(game)
a()

