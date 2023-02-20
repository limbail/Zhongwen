import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS words_table(word TEXT)')


def add_data(word):
    c.execute('INSERT INTO words_table(word) VALUES(?)', (word,))
    conn.commit()
