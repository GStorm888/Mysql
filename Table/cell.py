import pygame as pg


class Cell:
    def __init__(self, size, text, font_size,
                 color=pg.color.THECOLORS["azure"],
                 text_color=pg.color.THECOLORS["black"]):
        self._size = size
        self._color = color
        self._text = text
        self._font = pg.font.Font(None, font_size)
        self._text_color = text_color

    def draw(self, x: int, y: int, surface: pg.Surface):
        rect = pg.Rect(x, y, self._size, self._size)
        pg.draw.rect(surface, self._color, rect)

        text_surface = self._font.render(str(self._text), True, self._text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

    def size(self):
        return self._size