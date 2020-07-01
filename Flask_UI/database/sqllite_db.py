import sqlite3
from sqlite3 import Error

class DB:
    def __init__(self, connectionName):
        self.connectionName = connectionName
        self.connection = sqlite3.connect("file::memory:?cache=shared")
        self.version = sqlite3.version

    def connectionName(self):
        return self.connectionName

    def connection(self):
        return self.connection

    def version(self):
        return self.version

def more_info_insert(db_conn):
    c = db_conn.cursor()

    # create table
    c.execute('''CREATE TABLE IF NOT EXISTS web_values (page,property_name,value)''')
    c.execute('''INSERT INTO web_values VALUES('more_info', 'h1', 'This is a facial recognition media player')''')

    # commit the changes to db
    db_conn.commit()


def select_page(db_conn, page_name):
    c = db_conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS web_values (page,property_name,value)''')
    c.execute("SELECT * FROM web_values WHERE page = '" + page_name + "'")
    rows = c.fetchall()
    return rows