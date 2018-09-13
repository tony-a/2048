import random 
import copy


class Game():
    def __init__(self, grid_size):
        """
        (row, column)
        """
        self.grid = {}
        for x in range(0, grid_size):
            for y in range(0, grid_size):
                self.grid[x, y] = 0

        self.grid_size = grid_size
        self._add_random_value()
        self._add_random_value()

    def __repr__(self):
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

        return grid

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

    def add_row(self, row):
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

        while len(new) < len(row):
            new.append(0)

        return new

    def rows(self):
        for x in range(0, self.grid_size):
            row = []
            for y in range(0, self.grid_size):
                row.append(self.grid[x, y])
            yield row

    def swipe_left(self):
        new_grid = {}
        for row_index, row in enumerate(self.rows()):
            added_row = self.add_row(row)
            for x, value in enumerate(added_row):
                new_grid[row_index, x] = value

        # random_added = False
        if self.grid != new_grid:
            self.grid = new_grid
            self._add_random_value()
        
        return self

# x = [[2,2,0,4],[2,0,4,8],[0,0,2,4], [4,2,4,0]]
# y = [[0,2,0,0],[2048,0,4,8],[128,64,2,4], [4,2,4,0]]


# class Grid():
#     def __init__(self, grid_size):
#         self.grid_size = grid_size
#         row = [0 for x in range(0, grid_size)]
#         self.grid = [copy.deepcopy(row) for x in range(0, grid_size)]
#         x = random.randint(0, grid_size-1)
#         y = random.randint(0, grid_size-1)
#         self.grid[x][y] = 2

#         x2 = random.randint(0, grid_size-1)
#         y2 = random.randint(0, grid_size-1)
#         self.grid[x2][y2] = 2

#     def __repr__(self):
#         """
#         ---------------------
#         |    |    |    |2048|
#         ---------------------
#         |    |    |    | 4  |
#         ---------------------
#         |    | 64 |    | 4  |
#         ---------------------
#         |    |    | 2  | 2  |
#         ---------------------
#         """
#         cell_map = {0: '|    ', 
#                     2: '| 2  ',
#                     4: '| 4  ',
#                     8: '| 8  ',
#                     16: '| 16 ',
#                     32: '| 32 ',
#                     64: '| 64 ',
#                     128: '| 128',
#                     256: '| 256',
#                     512: '| 512',
#                     1024: '|1024',
#                     2048: '|2048',
#                     4096: '|4096'}
#         line_size =  4 * self.grid_size + self.grid_size + 1
#         grid = '-' * line_size + '\n'
        
#         for row in self.grid:
#             for index, cell in enumerate(row):
#                 grid += cell_map[cell]
#                 if index == self.grid_size - 1:
#                     grid += '|'
                
#             grid += '\n' + '-' * line_size + '\n'

#         return grid

#     # def __getitem__(self, x):
#     #     return self.grid[x]

#     def _strip_zero(row):
#         new = []
#         for item in row:
#             if item != 0:
#                 new.append(item)

#         return new

#     def add_row(self):
#         row = self.grid[0]
#         a = 0
#         b = 1
#         new = []
#         arr = _strip_zero(row)
#         while a < len(arr):
#             try:
#                 if arr[a] == arr[b]:
#                     new.append(arr[a] + arr[b])
#                     a += 2
#                     b += 2
#                 else:
#                     new.append(arr[a])
#                     a += 1
#                     b += 1
#             except IndexError:
#                 if a < len(arr):
#                     new.append(arr[a])

#         while len(new) < len(row):
#             new.append(0)

#         return new

#     def swipe_left(self):
#         new_grid = []
#         for row in self.grid:
#             new_grid.append(add_row(row))

#         random_added = False

#         self.grid = new_grid



# if __name__ == '__main__':
#     print "hi"
#     Grid2(4)



