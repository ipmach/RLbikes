# RLbikes

Working progress.

## API

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

Game manager controls:

``` python
  def __getitem__(item): pass  # Get game instance
  def start_game(game_index): pass  # Start game
  # Apply move in game
  def apply_move(game_index, bike, move, speed): pass  
  def get_timestep(game_index): pass  # Get timestep game
  def view_plt(game_index): pass  # Plot in matplotlib game
  def is_over(game_index): pass  # Get board of the game
  # Get bike view of the game
  def get_bike(game_index, bike, range_, mono=False, rotate=False): pass
````

## View example

In the left view of the board and in the right possible view of one bike. (Game interface not yet implemented.)

![Graph](https://github.com/ipmach/RLbikes/blob/main/Documentation/plt_img.png)
