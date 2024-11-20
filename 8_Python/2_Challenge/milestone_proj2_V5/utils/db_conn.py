"""
for using the class with "with" keyword, it is important to use 2 dunder methods
one is enter and another is exit

"""

import sqlite3

class database_connection:
    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
