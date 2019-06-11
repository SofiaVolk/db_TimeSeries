import sqlite3

conn = sqlite3.connect('mySQLiteDB.db')
cursor = conn.cursor()  # cursor - объект взаимодействия с бд


try:
    cursor.execute('CREATE TABLE weather (station text, date text, lan text, longt text, wind_dir text, wind_speed)')
except:
    pass


def insert_to_sqlite(data):
    cursor.executemany('INSERT INTO weather VALUES (?,?,?,?,?,?)', data)
    # cursor.execute(f'INSERT INTO weather VALUES {data}')
    conn.commit()  # сохранение изменений


