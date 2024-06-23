import pygame
import sys
from Table.row import Row
from Table.cell import Cell
from Table.table import Table
from table_seeder import TableSeeder

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tables")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # cell1_1 = Cell(188, "10", 100)
    # cell1_2 = Cell(188, "11", 100)
    # row1 = Row([cell1_1, cell1_2])
    # row1.draw(0, 0, screen)
    # cell2_1 = Cell(188, "100", 100)
    # cell2_2 = Cell(188, "101", 100)
    # row2 = Row([cell2_1, cell2_2])
    # row1.draw(0, 0, screen)

    seeder = TableSeeder() 
    table = seeder.generate_table("date_realise", False)

    table.draw(0, 0, screen)
    pygame.display.flip()


pygame.quit()
sys.exit()