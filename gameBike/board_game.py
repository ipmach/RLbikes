from gameBike.keys import Key
import numpy as np


class TableGame:

    def __init__(self, shape=(50, 50), bikes=[[25, 10], [25, 40]], load_map=None):
        """
        Initialize Table of the gameBike
        :param shape: actual shape of the board
        """
        # Initialize board
        if load_map is None:
            self.board = np.zeros(shape)
            load_map = 'Basic'
        else:  # Load define map
            self.board = np.load(load_map)
        # Always add borders and check walls are 1 and rest 0
        self.board[0, :] = np.ones(shape[0])
        self.board[shape[0] - 1, :] = np.ones(shape[0])
        check_walls = np.vectorize(lambda x: 1 if x > 1 else x)
        self.board = check_walls(self.board)
        # Add borders
        for i in range(1, self.board.shape[0]):
            self.board[i, 0] = 1
            self.board[i, shape[1] - 1] = 1
        # Initialize bikes
        self.bikes = np.array(bikes)
        self.alive = np.array([[True] for _ in range(len(self.bikes))])
        self.bikes_orientation = [Key.RIGHT, Key.LEFT]
        self.speeds = [1, 2, 3]
        for j, p in enumerate(self.bikes):
            self.apply(j, p, 1)
        self.status = {"Map": load_map, "Number bikes": len(self.bikes),
                       "Joined gameBike": 0, "Status": 'Waiting players'}

    def get_status(self):
        return self.status

    def apply(self, bike, pos, num):
        """
        Apply pixel update in the board
        :param bike: bike number
        :param pos: (x,y) coordinates
        :param num: new value
        :return:
        """
        if self.alive[bike]:  # Only update if bike still alvie
            self.board[pos[0]][pos[1]] = num

    def remove_bike(self, bike):
        """
        Remove bike and wall from the board
        :param bike: bike number
        :return:
        """
        self.board[self.bikes[bike][0]][self.bikes[bike][1]] = 0
        shape = self.board.shape
        board = self.board.reshape(-1)
        index = np.array(list(map(lambda x: (x == bike + 3), board)))
        index = np.nonzero(index)[0]
        board[index] = np.zeros(len(index))
        self.board = self.board.reshape(shape)
        print('I remove bike', bike, self.board[self.bikes[bike][0]][self.bikes[bike][1]])

    def apply_round(self, moves):
        """
        Apply round moves for time t
        :param moves: moves for time t
        :return:
        """
        self.old_board = np.copy(self.board)
        for i in range(moves.shape[0]):
            for j, p in enumerate(self.bikes):
                self.apply(j, p, j + 3)
            self.bikes = np.array(self.bikes + moves[i] * self.alive).astype(int)
            for j, p in enumerate(self.bikes):
                if self.board[p[0]][p[1]] > 0 and not np.all(moves[i][j] == [0, 0]):
                    if self.alive[j]:  # Only remove onces
                        self.alive[j] = False
                        self.remove_bike(j)
                else:
                    self.apply(j, p, 1)

    def is_over(self):
        """
        Return True if there is only one bike standing
        :return: Bool
        """
        return True if np.sum(self.alive.reshape(-1)) <= 1 else False

    def new_move(self):
        """
        Initialize new move for t+1
        (by default all bikes are moving forward at speed 1)
        :return: new initialize move
        """
        aux = np.zeros((3, self.bikes.shape[0], 2))
        for i in range(self.bikes.shape[0]):
            aux = self.add_move(i, aux, Key.FORWARD, 1)
        return aux

    def add_move(self, bike, moves, move, speed):
        """
        Add bike move to the gameBike
        :param bike: number bike
        :param moves: list of moves
        :param move: move to do
        :param speed: Speed of the bike
        :return: return moves update it
        """
        if move == Key.TURN_RIGHT:
            self.orientation_right(bike)
        elif move == Key.TURN_LEFT:
            self.orientation_left(bike)
        if self.bikes_orientation[bike] == Key.RIGHT:
            do_ = [0, 1]
        elif self.bikes_orientation[bike] == Key.UP:
            do_ = [1, 0]
        elif self.bikes_orientation[bike] == Key.LEFT:
            do_ = [0, -1]
        else:
            do_ = [-1, 0]
        moves[0][bike] = do_
        for i in range(speed):
            moves[i][bike] = do_
        return moves

    def orientation_left(self, bike):
        """
        Update orientation bike when turn left
        :param bike: number bike
        :return:
        """
        if self.bikes_orientation[bike] == Key.RIGHT:
            self.bikes_orientation[bike] = Key.UP
        elif self.bikes_orientation[bike] == Key.UP:
            self.bikes_orientation[bike] = Key.LEFT
        elif self.bikes_orientation[bike] == Key.LEFT:
            self.bikes_orientation[bike] = Key.DOWN
        else:
            self.bikes_orientation[bike] = Key.RIGHT

    def orientation_right(self, bike):
        """
        Update origntation bike when turn right
        :param bike: number bike
        :return:
        """
        if self.bikes_orientation[bike] == Key.RIGHT:
            self.bikes_orientation[bike] = Key.DOWN
        elif self.bikes_orientation[bike] == Key.UP:
            self.bikes_orientation[bike] = Key.RIGHT
        elif self.bikes_orientation[bike] == Key.LEFT:
            self.bikes_orientation[bike] = Key.UP
        else:
            self.bikes_orientation[bike] = Key.LEFT