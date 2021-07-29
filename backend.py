from gameBike.game_manager import GameManager
from flask import render_template
from flask import request
from flask import Flask
import numpy as np
import json

app = Flask(__name__)
path_games = "executions/example_execution.json"
games = GameManager(path_games)


@app.route('/')
def status():
    """
    Return status of server
    :return: status
    """
    aux = {"Number games": len(games), "Path execution": path_games}
    for j, game in enumerate(games.games_status):
        aux["Game " + str(j)] = game
    return aux


@app.route('/status')
@app.route('/status/<game>')
def status_games(game=None):
    """
    Return status of the games or a specific gameBike
    :param game: index gameBike for a specific gameBike
    :return: status
    """
    if game is None:
        aux = {}
        for i in range(len(games)):
            aux["Game " + str(i)] = games.games_status[i]['Status']
        return aux
    else:
        game = int(game)
        return {"Game " + str(game): games.games_status[game]['Status']}


@app.route('/join/<game>')
def join_game(game):
    """
    Request join a gameBike
    :param game: index gameBike
    :return: confirmation
    """
    game = int(game)
    if 0 > game or game > len(games):
        return "Not a valid gameBike"
    if games.join_game(game):
        return "Registration done"
    else:
        return "Not valid registration"


def format_view(view):
    matrix = ""
    index = np.nonzero(view)
    data = view[index]
    index = np.array(index).T
    for z, [i, j] in enumerate(index):
        matrix += str(i) + "," + str(j) + "," + str(data[z]) + " "
    return matrix

@app.route('/view/board/full/<game>')
def view_game(game):
    """
    Get view of a gameBike
    :param game: index gameBike
    :return: view gameBike
    """
    game = int(game)
    return {"Board_view": format_view(games.get_board(game)),
            "TimeStep": games.get_timestep(game)}


@app.route('/view/board/update/<game>')
def view_game_update(game):
    """
    Get view of a gameBike only update pixels
    :param game: index gameBike
    :return: view gameBike
    """
    game = int(game)
    if games.games_status[game]['Status'] == 'Running':
        return {"Board_view": format_view(games.get_board(game, only_update=True)),
                "TimeStep": games.get_timestep(game),
                "Status": games.games_status[game]['Status'],
                "NBikes": games.games_status[game]["Number bikes"],
                "OnlineBikes": games.games_status[game]["Joined gameBike"],
                "Map": games.games_status[game]["Map"],
                "Game": game}
    else:
        return {"Board_view": {},
                "TimeStep": games.get_timestep(game),
                "Status": games.games_status[game]['Status'],
                "NBikes": games.games_status[game]["Number bikes"],
                "OnlineBikes": games.games_status[game]["Joined gameBike"],
                "Map": games.games_status[game]["Map"],
                "Game": game}


def return_view(game, data):
    """
    Return view of the bike (POST)
    :param game: gameBike indedx
    :param data: dictionary with data need it
    :return: view bike
    """
    bike = data["bike"]
    range_ = data["range"]
    mono = data["mono"]
    rotate = data["rotate"]
    return {"Board_view": str(games.get_bike(game, bike, range_, mono=mono, rotate=rotate,
                                             compress=True)).replace("\n", "").replace("\t", " "),
            "TimeStep": games.get_timestep(game),
            "Status": games.games_status[game]['Status'],
            "Alive": "alive" if games.is_alive(game, bike) else "death"}


@app.route('/view/bike/<game>', methods=['GET', 'POST'])
def view_bike(game):
    """
    Get view of the bike (POST)
    :param game: gameBike index
    :return: view bike
    """
    game = int(game)
    if request.method == 'POST':
        data = json.loads(request.get_json())
        return return_view(game, data)
    return "Must be a POST request"


@app.route('/play/<game>', methods=['GET', 'POST'])
def play_bike(game):
    """
    Make move in gameBike (POST), also con return view bike
    :param game: gameBike index
    :return: view bike or confirmation
    """
    game = int(game)
    if request.method == 'POST':
        data = json.loads(request.get_json())
        bike = data['bike']
        move = data['move']
        speed = data['speed']
        games.apply_move(game, bike, move, speed)
        if data['return']:
            return return_view(game, data)
        else:
            return "OK"
    return "Must be a POST request"


@app.route('/visualizer/<game>')
def game(game):
    return render_template('visualizer.html', data={'num': game})