-- Create the bands table
CREATE TABLE IF NOT EXISTS bands (
                                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     name TEXT NOT NULL,
                                     hometown TEXT NOT NULL
);

-- Create the venues table
CREATE TABLE IF NOT EXISTS venues (
                                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      title TEXT NOT NULL,
                                      city TEXT NOT NULL
);

-- Create the concerts table (after bands and venues)
CREATE TABLE IF NOT EXISTS concerts (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        date TEXT NOT NULL,
                                        band_id INTEGER,
                                        venue_id INTEGER,
                                        FOREIGN KEY (band_id) REFERENCES bands(id),
                                        FOREIGN KEY (venue_id) REFERENCES venues(id)
);
