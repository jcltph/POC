"""
2048 game.
http://www.codeskulptor.org/#user40_xGLEQ9j9sb_68.py
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._width = grid_width
        self._height = grid_height
        
        self._start_tiles = {
            UP : [[0,ind] for ind in range(self._width)],
            DOWN : [[self._height - 1,ind] for ind in range(self._width)],
            LEFT : [[ind,0] for ind in range(self._height)],
            RIGHT : [[ind, self._width - 1] for ind in range (self._height)]
        }
     
        self._grid = [[0 for dummy_col in range(self._width)] 
                        for dummy_row in range(self._height)]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self.get_grid_width())] 
                        for dummy_row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_value = random.choice([2] * 9 + [4])
        new_pos_list = []
        
        for dummy_row in range(self._height):
            for dummy_col in range(self._width):
                if self._grid[dummy_row][dummy_col] == 0:
                    new_pos_list.append([dummy_row,dummy_col])
                    
        if not new_pos_list:
            print "GAME OVER"
        else:
            new_tile = random.choice(new_pos_list)
            self.set_tile(new_tile[0],new_tile[1],new_value)

    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for dummy_row in range(self._height):
            string += str(self._grid[dummy_row])+"\n"
        return string

    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        init_tiles_ind = self._start_tiles[direction]
        start_grid = str(self._grid)
        
        if (direction == UP) or (direction == DOWN):
            length = self._height   
        elif (direction == LEFT) or (direction == RIGHT):
            length = self._width
        else: 
            print "Illegal Move"
        
        for init_ind in init_tiles_ind:
            temp_line = []
            for step in range(length):
                temp_ind_row = init_ind[0] + step*OFFSETS[direction][0]
                temp_ind_col = init_ind[1] + step*OFFSETS[direction][1]
                temp_tile = self.get_tile(temp_ind_row,temp_ind_col)
                temp_line.append(temp_tile)
                
            temp_line = merge(temp_line)
                
            for step in range(length):
                temp_ind_row = init_ind[0] + step*OFFSETS[direction][0]
                temp_ind_col = init_ind[1] + step*OFFSETS[direction][1]
                self.set_tile(temp_ind_row,temp_ind_col,temp_line[step])
        
        finish_grid = str(self._grid)
        
        if start_grid != finish_grid:
            self.new_tile()

    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line_copy = list(line)
    line_merge = [0] * len(line)
    counter = 0
    
    if len(line_copy) == 1: 
        return(line_copy)
    
    for pos in range(0,len(line_copy)-1):
        if line_copy[pos] > 0:
            match = findmatching(line_copy,pos)
            if match[0] != 0:
                line_copy[pos] *= 2
                line_copy[match[1]] = 0
                line_merge[counter] = line_copy[pos]
                counter += 1
            else:
                line_merge[counter] = line_copy[pos]
                counter += 1
                
    line_merge[counter] = line_copy[-1]
    return line_merge

def findmatching(line,pos):
    """
    Helper function for merge. 
    """
    while True:
        for ind in range(pos+1,len(line)):
            if (line[ind] == 0) and (ind != len(line)-1):
                continue
            elif (line[ind] != 0) and (line[ind] != line[pos]):
                return([0,-1])
            elif (line[ind] != 0) and (line[ind] == line[pos]):
                return([line[ind],ind])
            else:
                return([0,-1])

poc_2048_gui.run_gui(TwentyFortyEight(6, 4))

