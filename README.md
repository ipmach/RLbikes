# RLbikes

Working progress.

## Server

To build the server:

``` bash
docker build -t server .
````

To execute the server:

``` bash
docker run -p 5000:5000 server .
````

### Server API (http requests)

``` bash
IP/  # General info
IP/status  # Status of all games
IP/status/<game>  # Status of a game
IP/join/<game>  # Request join game
IP/view/board/full/<game>  # Get a view of a game
IP/view/board/update/<game>  # Get a view of the updated game
IP/play/<game>  # Add a move in the game, body: {bike: int, move: int, speed: int}
IP/visualizer/<game>  # Visualize game with html interface
````

### Game view examples

Some visualizations.

#### Agent visualization

Two possible examples of what the IA can see, in the left view of the board and in the right possible view of one bike. 

<img src="https://github.com/ipmach/RLbikes/blob/main/Documentation/plt_img.png" alt="drawing" width="400"/>

#### HTML visualization (working progress)

Default visualization for humans.

<img src="https://github.com/ipmach/RLbikes/blob/main/Documentation/human_interface.PNG" alt="drawing" width="400"/>

### Server internal functions

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
