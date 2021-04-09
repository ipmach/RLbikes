import matplotlib.pyplot as plt
from game import Game
from keys import Key


tg = Game(load_map='maps/map_1.npy')
moves = tg.new_move()
moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
tg.apply_round(moves)

print(tg.is_over())

moves = tg.new_move()
moves = tg.add_move(1, moves, Key.FORWARD, 2)
tg.apply_round(moves)

moves = tg.new_move()
moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
tg.apply_round(moves)

moves = tg.new_move()
moves = tg.add_move(1, moves, Key.TURN_RIGHT, 2)
moves = tg.add_move(0, moves, Key.TURN_RIGHT, 3)
tg.apply_round(moves)

moves = tg.new_move()
moves = tg.add_move(1, moves, Key.TURN_RIGHT, 2)
moves = tg.add_move(0, moves, Key.TURN_LEFT, 3)
tg.apply_round(moves)

moves = tg.new_move()
moves = tg.add_move(1, moves, Key.TURN_RIGHT, 2)
moves = tg.add_move(0, moves, Key.FORWARD, 3)
tg.apply_round(moves)

moves = tg.new_move()
#moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
moves = tg.add_move(0, moves, Key.TURN_LEFT, 3)
tg.apply_round(moves)

moves = tg.new_move()
#moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
moves = tg.add_move(0, moves, Key.TURN_LEFT, 3)
tg.apply_round(moves)

moves = tg.new_move()
#moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
moves = tg.add_move(0, moves, Key.TURN_RIGHT, 3)
tg.apply_round(moves)

moves = tg.new_move()
#moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
moves = tg.add_move(0, moves, Key.FORWARD, 2)
tg.apply_round(moves)

tg.get_view_board()

moves = tg.new_move()
#moves = tg.add_move(1, moves, Key.TURN_LEFT, 2)
moves = tg.add_move(0, moves, Key.FORWARD, 1)
tg.apply_round(moves)

moves = tg.new_move()
moves = tg.add_move(0, moves, Key.FORWARD, 3)
tg.apply_round(moves)
print(moves)

print(tg.alive)
print(tg.is_over())
print(tg.get_view_board(only_update=True, compress=True))

fig = plt.figure(1)
plt.subplot(121)
plt.imshow(tg.get_view_board(only_update=False))
plt.subplot(122)
plt.imshow(tg.get_view_bike(0, 20, rotate=True, mono=True))
plt.colorbar()
plt.figure(2)
plt.imshow(tg.get_view_board(only_update=True))
plt.show()
