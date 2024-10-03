import sqlite3


class Band:
    def __init__(self, band_id, name, hometown):
        self.id = band_id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def find(band_id):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM bands WHERE id = ?", (band_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Band(*row)

    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT c.date, v.title 
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            WHERE c.band_id = ?
        ''', (self.id,))
        concerts = cur.fetchall()
        conn.close()
        return concerts

    def venues(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT DISTINCT v.title, v.city
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            WHERE c.band_id = ?
        ''', (self.id,))
        venues = cur.fetchall()
        conn.close()
        return venues

    def play_in_venue(self, venue_title, date):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("SELECT id FROM venues WHERE title = ?", (venue_title,))
        venue_id = cur.fetchone()[0]
        cur.execute("INSERT INTO concerts (date, band_id, venue_id) VALUES (?, ?, ?)", (date, self.id, venue_id))
        conn.commit()
        conn.close()

    def all_introductions(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT v.city, b.name, b.hometown 
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            JOIN bands b ON c.band_id = b.id
            WHERE c.band_id = ?
        ''', (self.id,))
        concerts = cur.fetchall()
        conn.close()
        introductions = [f"Hello {city}!!!!! We are {self.name} and we're from {self.hometown}" for city, name, hometown
                         in concerts]
        return introductions

    