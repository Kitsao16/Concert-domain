import sqlite3


def setup_db():
    conn = sqlite3.connect('concerts.db')
    cur = conn.cursor()

    # Run migrations
    with open('migrations/001_create_bands_table.sql', encoding='utf-8') as f:
        cur.executescript(f.read())
    with open('migrations/002_create_venues_table.sql', encoding='utf-8') as f:
        cur.executescript(f.read())
    with open('migrations/003_create_concerts_table.sql', encoding='utf-8') as f:
        cur.executescript(f.read())

    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_db()
