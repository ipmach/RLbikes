from heuristic_basic import BasicHeuristic
from game_manager import GameManager
import numpy as np

a = GameManager("executions/example_execution.json")
(run, _) = a[0]
a.start_game(0)
#a.start_game(1)
heuristic = BasicHeuristic()
t = -1
while not a.is_over(0):
    a.view_plt(0)
    t_aux = a.get_timestep(0)
    if t < t_aux:
        view = a.get_bike(0, 0, 3, mono=True, rotate=True)
        a.apply_move(0, 0, heuristic(view), 1)
        view = a.get_bike(0, 1, 3, mono=True, rotate=True)
        a.apply_move(0, 1, heuristic(view), 2)
        t = t_aux

a.view_plt(0)
np.save("test.npy", a.get_bike(0,0, 3, mono=True, rotate=True))




