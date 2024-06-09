from data_base import Database

class Books:

    @staticmethod
    def get_dy_id(books_id: int):
        stmt = "SELECT * FROM Books WHERE id=%s;"
        Database.cursor().execute(stmt, [books_id])
        return Database.cursor().fetchone()
    
    @staticmethod
    def get_all():
        stmt = "SELECT * FROM Books;"
        Database.cursor().execute(stmt)
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
    