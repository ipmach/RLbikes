# RLbikes

Game controls:

``` python
  def new_move(): pass  # Initialize new move t
  def add_move(bike, moves, move, speed): pass
  def apply_round(moves): pass  # Apply round t
  def get_view_bike(bike, view_range, rotate, mono): pass
  def get_view_board(only_update, compress): pass
````

Run game controls:

``` python
  def get_moves(): pass  # Access pointer matrix moves
  def get_t(): pass  # Get t value
  def view_plt(): pass  # view game with plt
  def __call__(): pass  # start game
````
