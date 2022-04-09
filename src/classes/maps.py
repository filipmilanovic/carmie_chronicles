import numpy as np
import os
from random import sample

from classes.cells import Cell

map_dict = {}


class Map:
    """Map class object, comprised of a series of Cells to generate a grid"""
    instances = []

    def __init__(self,
                 rows: int,
                 cols: int,
                 towns: int):
        self.hash = hash(self)
        map_dict[self.hash] = self
        self.rows = rows
        self.cols = cols
        self.cells = None
        self.grid = None

        self.generate_cells()
        self.generate_towns(towns)
        self.generate_grid()
        self.link_cells()

    def generate_cells(self):
        """generate the Cells to populate the Map given the size of the grid"""
        self.cells = [Cell() for i in range(0, self.rows * self.cols)]

    def generate_towns(self,
                       number_towns: int):
        """randomly designate Cells to be towns"""
        [setattr(cell, 'is_town', True) for cell in sample(self.cells, number_towns)]
        [cell.update_appearance(False) for cell in self.cells]

    def generate_grid(self):
        """reshape list of Cells into a grid"""
        self.grid = np.reshape([cell.appearance for cell in self.cells], (self.rows, self.cols))

    def link_cells(self):
        """provide mapping of Cells to other Cells, then generate possible actions"""
        for cell in range(len(self.cells)):
            current_cell = self.cells[cell]
            if (cell % self.cols) != 0 & (cell > 0):
                current_cell.west_hash = self.cells[cell - 1].hash
            if ((cell+1) % self.cols != 0) & (cell < self.cols * self.rows - 1):
                current_cell.east_hash = self.cells[cell + 1].hash
            if cell >= self.cols:
                current_cell.north_hash = self.cells[cell - self.cols].hash
            if cell < (self.cols-1) * self.rows:
                current_cell.south_hash = self.cells[cell + self.cols].hash

    def print(self):
        os.system('clear')
        print(self.grid)
