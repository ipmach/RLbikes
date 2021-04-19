from heuristic_basic import BasicHeuristic
from game_manager import GameManager
import matplotlib.pyplot as plt

a = GameManager("executions/example_execution.json")
(run, _) = a[0]


heuristic = BasicHeuristic(deterministic=False)
heuristic2 = BasicHeuristic(deterministic=False)
heuristic3 = BasicHeuristic(deterministic=True)
heuristic4 = BasicHeuristic(deterministic=True)
t = -1
view = a.get_bike(0, 0, 6, mono=True, rotate=True)
view2 = a.get_bike(0, 1, 6, mono=True, rotate=True)
a.start_game(0)
a.start_game(1)

view_size1, mono1, rotate1 = heuristic.request_view()
view_size2, mono2, rotate2 = heuristic2.request_view()
view_size3, mono3, rotate3 = heuristic3.request_view()
view_size4, mono4, rotate4 = heuristic4.request_view()

while not a.is_over(0) or not a.is_over(1):
    t_aux = a.get_timestep(0)
    view = a.get_bike(0, 0, view_size1, mono=mono1, rotate=rotate1)
    move, speed = heuristic(view, t_aux)
    if move != -1:
        a.apply_move(0, 0, move, speed)
    view = a.get_bike(0, 1, view_size2, mono=mono2, rotate=rotate2)
    move, speed = heuristic2(view, t_aux)
    if move != -1:
        a.apply_move(0, 1, move, speed)

    t_aux2 = a.get_timestep(1)
    view = a.get_bike(1, 0, view_size3, mono=mono3, rotate=rotate3)
    move, speed = heuristic3(view, t_aux2)
    if move != -1:
        a.apply_move(1, 0, move, speed)
    view = a.get_bike(1, 1, view_size4, mono=mono4, rotate=rotate4)
    move, speed = heuristic4(view, t_aux2)
    if move != -1:
        a.apply_move(1, 1, move, speed)

    plt.subplot(1, 2, 1)
    plt.title("Game 1 t: " + str(t_aux))
    plt.imshow(a.get_board(0))
    plt.subplot(1, 2, 2)
    plt.title("Game 2 t: " + str(t_aux2))
    plt.imshow(a.get_board(1))
    plt.pause(0.1)
    plt.clf()

plt.title("Game 0 t: " + str(t_aux))
plt.imshow(a.get_board(0))
plt.subplot(1, 2, 2)
plt.title("Game 1 t: " + str(t_aux2))
plt.imshow(a.get_board(1))
plt.show()




