import pygame
from Table.cell import Cell
class Row:
    def __init__(self, cells: list):
        self._gap = 10
        self._cells = cells       

    def draw(self, x: int, y: int, surface: pygame.Surface):
        current_x = x
        for cell in self._cells:
            cell.draw(current_x, y, surface)
            current_x += self._gap + cell.size()
    
    def height(self):
        return self._cells[0].size()