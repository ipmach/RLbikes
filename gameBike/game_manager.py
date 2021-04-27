from gameBike.run_game import RunGame
from gameBike.game import Game
import threading
import json


class GameManager:

    def __init__(self, execution_path):
        """
        Manage different games
        :param execution_path: execution path games
        """
        self.list_threads = []
        self.list_games = []
        self.games_status = []
        execution = json.load(open(execution_path))
        for game in execution['Games']:
            map = game['map']
            if map == "":
                map = None
            aux = Game(load_map=map,
                       bikes=game['bikes'])
            self.games_status.append(aux.get_status())
            self.list_games.append(RunGame(aux, view=False,
                                           time_=float(game['time'])))
            self.list_threads.append(threading.Thread(
                target=self.list_games[-1],
                args=()))

    def __getitem__(self, item):
        """
        Get gameBike instance
        :param item:
        :return: (running_game, thread_game)
        """
        return self.list_games[item], self.list_threads[item]

    def __len__(self):
        return len(self.list_games)

    def join_game(self, game):
        if self.games_status[game]["Joined gameBike"] == self.games_status[game]["Number bikes"]:
            return False
        elif self.games_status[game]["Joined gameBike"] < self.games_status[game]["Number bikes"]:
            self.games_status[game]["Joined gameBike"] += 1
            if self.games_status[game]["Joined gameBike"] == self.games_status[game]["Number bikes"]:
                self.start_game(game)
            return True


    def start_game(self, game_index):
        """
        Start gameBike
        :param game_index: index gameBike
        :return:
        """
        self.games_status[game_index]['Status'] = "Running"
        (_, thread) = self[game_index]
        thread.start()

    def apply_move(self, game_index, bike, move, speed):
        """
        Apply move in gameBike
        :param game_index: index gameBike
        :param bike: number bike
        :param move: move we want to apply
        :param speed: speed bike
        :return:
        """
        (run, _) = self[game_index]
        moves = run.get_moves()
        run.game.add_move(bike, moves, move, speed)

    def get_timestep(self, game_index):
        """
        Get timestep gameBike
        :param game_index:  index gameBike
        :return: timestep
        """
        (run, _) = self[game_index]
        return run.get_t()

    def view_plt(self, game_index):
        """
        Plot in matplotlib gameBike
        :param game_index: index gameBike
        :return:
        """
        (run, _) = self[game_index]
        run.view_plt()

    def is_over(self, game_index):
        """
        Check if the gameBike is over
        :param game_index: index gameBike
        :return: boolean
        """
        (run, _) = self[game_index]
        return run.game.is_over()

    def is_alive(self, game_index, bike):
        """
        Check if the bike is alive
        :param game_index: index gameBike
        :param bike: index bike
        :return: boolean
        """
        (run, _) = self[game_index]
        return run.game.alive[bike][0]

    def get_board(self, game_index, only_update=False, compress=False):
        """
        Get board of the gameBike
        :param game_index: index gameBike
        :param only_update: only updated pixels
        :param compress: return compress form
        :return: board
        """
        (run, _) = self[game_index]
        return run.game.get_view_board(only_update=only_update,
                                       compress=compress)

    def get_bike(self, game_index, bike, range_, mono=False, rotate=False, compress=True):
        """
        Get bike view of the gameBike
        :param game_index: index gameBike
        :param bike: number bike
        :param range_: range view bike
        :param mono: binary values ornot
        :param rotate: rotate view so bike always point same direction
        :param compress: return compress form
        :return: view bike
        """
        (run, _) = self[game_index]
        return run.game.get_view_bike(bike, range_, mono=mono, rotate=rotate, compress=compress)