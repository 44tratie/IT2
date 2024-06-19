import pygame as pg

from .cell import Cell

class Grid:
    """Represents the grid in the Game of Life. It is responsible for managing cells"""

    def __init__(self, window: pg.Surface, initial_cells: list[list[Cell]]) -> None:
        self.window = window
        self.cells = initial_cells

    def draw(self) -> None:
        """Draws the grid"""
        self._draw_grid()
        self._draw_cells()
    
    def _draw_grid(self) -> None:
        """Draws the lines to create a visual grid"""
        # assumes window is square, else two for loops (one for x, one for y) is needed
        for pos in range(0, self.window.get_width(), Cell.SIZE):
            pg.draw.line(self.window, "black", (pos, 0), (pos, self.window.get_height()))
            pg.draw.line(self.window, "black", (0, pos), (self.window.get_width(), pos))

    def _draw_cells(self) -> None:
        """Draws the cells to fill the grid"""
        for row in self.cells:
            for cell in row:
                cell.draw()

    def calculate_next_generation(self) -> None:
        """Calculates the next generation and updates cells according to the game rules"""
        # I choose to create new cells instead of creating an update method in the Cell class
        # (because cells die and are born between generations according to the rules)
        next_cells = []

        for row in self.cells:
            next_row = []
            for cell in row:
                neighbors = self._alive_neighbor_count(cell)

                if cell.is_alive:
                    # Cell should be alive is it has 2 or 3 alive neighbors and is alive itself
                    next_row.append(Cell(self.window, cell.x, cell.y, 2 <= neighbors <= 3))
                else:
                    # Cell should be alive is it has exactly 3 alive neighbors but is not alive
                    next_row.append(Cell(self.window, cell.x, cell.y, neighbors == 3))

            next_cells.append(next_row)
                
        self.cells = next_cells

    def _alive_neighbor_count(self, cell: Cell) -> int:
        """Gets the amount of alive neighbors of a cell"""
        alive = 0

        for n_row, n_col in self._get_neighbors(cell.row_i, cell.col_i):
            if self.cells[n_row][n_col].is_alive:
                alive += 1
        
        return alive

    def _get_neighbors(self, row_i: int, col_i: int) -> list[tuple[int, int]]:
        """Gets possible neighbors for a cell (excludes cells that are out of bounds)"""
        neighbors = []

        if not row_i == 0:
            # Cell above must be available
            # Top
            neighbors.append((row_i-1, col_i))

            # Top left
            if not col_i == 0:
                neighbors.append((row_i-1, col_i-1))
            
            # Top right
            if not col_i == len(self.cells[0]) - 1:
                neighbors.append((row_i-1, col_i+1))

        if not row_i == len(self.cells) - 1:
            # Cell below must be available
            neighbors.append((row_i+1, col_i))

            # Bottom left
            if not col_i == 0:
                neighbors.append((row_i+1, col_i-1))

            # Bottom right
            if not col_i == len(self.cells[0]) - 1:
                neighbors.append((row_i+1, col_i+1))

        # Direct left
        if not col_i == 0:
            neighbors.append((row_i, col_i-1))
        
        # Direct right
        if not col_i == len(self.cells[0]) - 1:
            neighbors.append((row_i, col_i+1))

        return neighbors
    
    def nullify(self) -> None:
        """Sets all cells to be not alive"""

        for row in self.cells:
            for cell in row:
                cell.is_alive = False

    def invert_cell(self, pos: tuple[int, int]) -> None:
        """Inverts a cell given coordinates (doesn't necessarily need to be mouse_pos)"""
        # Coordinates are usually written in (x, y) form so we need to flip it to (row, col)
        col_i, row_i = pos[0] // Cell.SIZE, pos[1] // Cell.SIZE

        # Get the targeted cell and invert its state
        cell = self.cells[row_i][col_i]
        cell.is_alive = not cell.is_alive
