from game_manager import GameManager
from flask import Flask

app = Flask(__name__)
path_games = "executions/example_execution.json"
games = GameManager(path_games)


@app.route('/')
def status():
    aux = {"Number games": len(games), "Path execution": path_games}
    for j, game in enumerate(games.games_status):
        aux["Game " + str(j)] = game
    return aux


@app.route('/status')
def status_games():
    aux = {}
    for i in range(len(games)):
        aux["Game " + str(i)] = games.games_status[i]['Status']
    return aux


@app.route('/status/<game>')
def status_game(game):
    game = int(game)
    return {"Game " + str(game): games.games_status[game]['Status']}


@app.route('/join/<game>')
def join_game(game):
    game = int(game)
    print(game < len(games))
    if 0 > game or game > len(games):
        return "Not a valid game"
    if games.join_game(game):
        return "Registration done"
    else:
        return "Not valid registration"


@app.route('/view/board/full/<game>')
def view_game(game):
    game = int(game)
    return {"Board_view": str(games.get_board(game,
                                              compress=True)).replace("\n","").replace("\t"," "),
            "TimeStep": games.get_timestep(game)}


@app.route('/view/board/update/<game>')
def view_game_update(game):
    game = int(game)
    if games.games_status[game]['Status'] == 'Running':
        return {"Board_view": str(games.get_board(game, only_update=True,
                                                  compress=True)).replace("\n","").replace("\t"," "),
                "TimeStep": games.get_timestep(game)}
    else:
        return "Game is not running"



