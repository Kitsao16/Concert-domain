import sqlite3


class Venue:
    def __init__(self, venue_id, title, city):
        self.id = venue_id
        self.title = title
        self.city = city

    @staticmethod
    def find(venue_id):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM venues WHERE id = ?", (venue_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Venue(*row)

    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT c.date, b.name
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            WHERE c.venue_id = ?
        ''', (self.id,))
        concerts = cur.fetchall()
        conn.close()
        return concerts

    def bands(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT DISTINCT b.name, b.hometown
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            WHERE c.venue_id = ?
        ''', (self.id,))
        bands = cur.fetchall()
        conn.close()
        return bands

    def concert_on(self, date):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT b.name
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            WHERE c.venue_id = ? AND c.date = ?
        ''', (self.id, date))
        band = cur.fetchone()
        conn.close()
        return band

    def most_frequent_band(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT b.name, COUNT(*) as performance_count
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            WHERE c.venue_id = ?
            GROUP BY b.id
            ORDER BY performance_count DESC
            LIMIT 1
        ''', (self.id,))
        band = cur.fetchone()
        conn.close()
        return band
