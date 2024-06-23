from Database.books import Books
from Table.row import Row
from Table.cell import Cell
from Table.table import Table

class TableSeeder:

    def __init__(self,):
        pass

    @staticmethod
    def generate_table( order_col: str, order_acending: bool):
        books = Books.get_all(order_col, order_acending)
        rows = []
        names = []

        for name in Books.get_column_names():
            names.append(Cell(100, name, 15))
            rows.append(Row(names))

        for book in books:
            cells = []
            for col in book:
                cells.append(Cell(100, col, 15))
            rows.append(Row(cells))

        return Table(rows)
