from game_manager import GameManager
import matplotlib.pyplot as plt
from keys import Key


a = GameManager("executions/example_execution.json")
(run, _) = a[0]
a.start_game(0)
a.start_game(1)

t = -1
while not a.is_over(0):
    a.view_plt(0)
    t_aux = a.get_timestep(0)
    if t < t_aux:
        a.apply_move(0, 1, Key.TURN_RIGHT, 3)
        t = t_aux
plt.imshow(a.get_board(0))
plt.show()


