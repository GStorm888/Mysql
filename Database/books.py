from Database.data_base import Database

class Books:

    @staticmethod
    def get_dy_id(books_id: int):
        stmt = "SELECT * FROM Books WHERE id=%s;"
        Database.cursor().execute(stmt, [books_id])
        return Database.cursor().fetchone()
    
    @staticmethod
    def get_all(order_col: str, order_acending: bool):
        order = "ASC" if order_acending else "DESC"
        stmt = f"SELECT * FROM Books ORDER BY {order_col} {order};"
        Database.cursor().execute(stmt, [])
        return Database.cursor().fetchall()
    
    @staticmethod
    def get_by_name(name):
        stmt = "SELECT * FROM Books WHERE name=%s;"
        Database.cursor().execute(stmt, [name])
        return Database.cursor().fetchall()

    @staticmethod
    def get_by_autor(autor):
        stmt = "SELECT * FROM Books WHERE autor=%s;"
        Database.cursor().execute(stmt, [autor])
        return Database.cursor().fetchall()
    
    @staticmethod
    def get_column_names():
        stmt = "SHOW COLUMNS FROM Books"
        Database.cursor().execute(stmt, [])
        names = []
        for row in Database.cursor().fetchall():
            names.append(row[0])
        return names