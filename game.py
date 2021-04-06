from table_game import TableGame
from keys import Key
import numpy as np


class Game(TableGame):

    def get_view_bike(self, bike, range, mono=False, rotate=False):
        """
        Get view of the bike
        :param bike: number bike
        :param range: range of view
        :param mono: binary image or not
        :param rotate: rotate the view so the bike is always looking same position
        :return:
        """
        coord = self.bikes[bike]

        low_x = coord[0] - range if coord[0] - range >= 0 else 0
        high_x = coord[0] + range + 1 if coord[0] + range + 1 < self.table.shape[0] else self.table.shape[0] - 1
        low_y = coord[1] - range if coord[1] - range >= 0 else 0
        high_y = coord[1] + range + 1 if coord[1] + range + 1 < self.table.shape[1] else self.table.shape[1] - 1

        view = self.table[low_x: high_x, low_y: high_y]

        if mono:
            reduce = np.vectorize(lambda x: x if x < 1 else 1)
            view = reduce(view)

        aux = np.ones((2 * range - 1, 2 * range - 1))

        if rotate:
            if self.bikes_orientation[bike] == Key.RIGHT:
                view = np.rot90(view, k=1)
            elif self.bikes_orientation[bike] == Key.LEFT:
                view = np.rot90(view, k=3)
            elif self.bikes_orientation[bike] == Key.UP:
                view = np.rot90(view, k=2)
            else:
                print("up")
        return view