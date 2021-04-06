import matplotlib.pyplot as plt
from game import Game
from keys import Key



tg = Game()
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


print(tg.alive)
print(tg.is_over())

plt.subplot(121)
plt.imshow(tg.table)
plt.subplot(122)
plt.imshow(tg.get_view_bike(0, 4, rotate=True, mono=True))
plt.colorbar()
plt.show()