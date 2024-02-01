import sqlite3

connection = sqlite3.connect('parkingo.db')
cursor = connection.execute()

def create_tables(
        connection:sqlite3.Connection=connection,
        cursor:sqlite3.Cursor=cursor
        ):
    queries = [
        '''
CREATE TABLE IF NOT EXISTS car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate VARCHAR(15) UNIQUE NOT NULL
);
''',
        '''
CREATE TABLE IF NOT EXISTS car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    duration_hours INTEGER,
    price_per_hour DECIMAL(18,2)
);
''',
        '''
CREATE TABLE IF NOT EXISTS car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arrival DATETIME NOT NULL,
    departure DATETIME,
    car_id INTEGEER REFERENCES car(id),
    tariff_id INTEGER REFERENCES tariff(id),
    total_price DECIMAL(18,2) DEFAULT 0
);
''',
    ]

    with connection:
        for query in queries:
            cursor.execute(query)

create_tables()
