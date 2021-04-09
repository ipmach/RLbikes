import matplotlib.pyplot as plt
from run_game import RunGame
from game import Game
from keys import Key
import threading

game = Game(load_map='maps/map_1.npy')
a = RunGame(game, view=False)

x = threading.Thread(target=a, args=())
x.start()
t = -1
while not a.game.is_over():
    a.view_plt()

    moves = a.get_moves()
    game.add_move(1, moves, Key.TURN_RIGHT, 3)
plt.imshow(a.game.get_view_board())
plt.show()


