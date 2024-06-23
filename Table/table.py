import pygame
from Table.row import Row
from Table.cell import Cell

class Table:
    def __init__(self, rows:list):
        self.gap = 10
        self.rows = rows
    
    def draw(self, x:int, y:int, surface: pygame.Surface):
        current_y = y
        for row in self.rows:
            row.draw(x, current_y, surface)
            current_y += self.gap + row.height()
