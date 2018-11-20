import random 
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

WIDTH = 35
HEIGHT = 20
TIMEOUT = 100


class Game():
    def __init__(self, grid_size):
        """
        (row, column)
        """
        if type(grid_size) != int or grid_size < 2:
            print "Why are you doing this?"
            grid_size = 4

        self.grid = {}
        for x in range(0, grid_size):
            for y in range(0, grid_size):
                self.grid[x, y] = 0

        self.grid_size = grid_size
        self._add_random_value()
        self._add_random_value()

    # def __repr__(self):
    def render(self, window):
        """
        ---------------------
        |    |    |    |2048|
        ---------------------
        |    |    |    | 4  |
        ---------------------
        |    | 64 |    | 4  |
        ---------------------
        |    |    | 2  | 2  |
        ---------------------
        """
        cell_map = {0: '|    ', 
                    2: '| 2  ',
                    4: '| 4  ',
                    8: '| 8  ',
                    16: '| 16 ',
                    32: '| 32 ',
                    64: '| 64 ',
                    128: '| 128',
                    256: '| 256',
                    512: '| 512',
                    1024: '|1024',
                    2048: '|2048',
                    4096: '|4096'}
        line_size =  4 * self.grid_size + self.grid_size + 1
        grid = '-' * line_size + '\n'
        
        for x in range(0, self.grid_size):
            for y in range(0, self.grid_size):
                grid += cell_map.get(self.grid[x, y], '|    ')

            grid += '|\n' + '-' * line_size + '\n'

        window.addstr(grid)
        # return grid

    # def __getitem__(self, x):
    #     return self.grid[x]

    def _add_random_value(self):
        x, y = random.choice([position for position, value in self.grid.items() if value == 0])
        self.grid[x, y] = 2

    def _strip_zero(self, row):
        new = []
        for item in row:
            if item != 0:
                new.append(item)

        return new

    def add_row(self, row, direction):
        a = 0
        b = 1
        new = []
        arr = self._strip_zero(row)
        while a < len(arr):
            try:
                if arr[a] == arr[b]:
                    new.append(arr[a] + arr[b])
                    a += 2
                    b += 2
                else:
                    new.append(arr[a])
                    a += 1
                    b += 1
            except IndexError:
                if a < len(arr):
                    new.append(arr[a])
                break

        return self._pad_zeros(new, direction)

    def _pad_zeros(self, row, direction):
        while len(row) < self.grid_size:
            if direction == 'l':
                row.append(0)
            else:
                row.insert(0, 0)

        return row


    def rows(self, transpose=False):
        """
        (row, column)
        """
        for row_index in range(0, self.grid_size):
            row = []
            for column_index in range(0, self.grid_size):
                if transpose:
                    row_index, column_index = column_index, row_index
                row.append(self.grid[row_index, column_index])
            yield row

    def columns(self):
        for column_index in range(0, self.grid_size):
            column = []
            for row_index in range(0, self.grid_size):
                column.append(self.grid[row_index, column_index])
            yield column

    def swipe_left(self):
        new_grid = {}
        for row_index, row in enumerate(self.rows()):
            added_row = self.add_row(row, 'l')
            for x, value in enumerate(added_row):
                new_grid[row_index, x] = value

        if self.grid != new_grid:
            self.grid = new_grid
            self._add_random_value()
        
        return self

    def swipe_right(self):
        new_grid = {}
        for row_index, row in enumerate(self.rows()):
            added_row = self.add_row(row, 'r')
            for x, value in enumerate(added_row):
                new_grid[row_index, x] = value

        if self.grid != new_grid:
            self.grid = new_grid
            self._add_random_value()
        
        return self

    def swipe_up(self):
        new_grid = {}
        for row_index, row in enumerate(self.columns()):
            added_row = self.add_row(row, 'l')
            for x, value in enumerate(added_row):
                new_grid[x, row_index] = value

        if self.grid != new_grid:
            self.grid = new_grid
            self._add_random_value()
        
        return self

    def swipe_down(self):
        new_grid = {}
        for row_index, row in enumerate(self.columns()):
            added_row = self.add_row(row, 'r')
            for x, value in enumerate(added_row):
                new_grid[x, row_index] = value

        if self.grid != new_grid:
            self.grid = new_grid
            self._add_random_value()

        return self

"""
reload(game)
g = game.Game(4)
g
"""

if __name__=='__main__':
    print "hii"
    curses.initscr()
    curses.beep()
    curses.beep()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    game = Game(4)

    while True:
        window.clear()
        window.border(0)
        game.render(window)
        event = window.getch()

        if event == 27:
            break

        if event == KEY_LEFT:
            game.swipe_left()

        elif event == KEY_RIGHT:
            game.swipe_right()

        elif event == KEY_UP:
            game.swipe_up()

        elif event == KEY_DOWN:
            game.swipe_down()


    curses.endwin()