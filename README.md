Concert-Domain
Concert-Domain is a Python-based application that allows users to manage bands, venues, and concerts. The project includes database interactions using SQLite to store information about bands, venues, and concerts, and provides functionalities for retrieving, updating, and inserting data. The application is primarily designed for music concert management, with the ability to track which band is performing at which venue and on which date.

Table of Contents
Project Structure
Database Design
Bands Table
Venues Table
Concerts Table
Database Interactions
Inserting Data
Querying Data
Updating Data
Main Functionalities
Band Class
Venue Class
Concert Class
main.py Overview
Setup
How to Run
Project Structure
The project consists of the following files:                                    Concert-domain/
│
├── models/
│   ├── band.py    
│   ├── venue.py             
│   ├── concert.py           
│
├── migrations/              
│   ├── 001_create_bands_table.sql  
│   ├── 002_create_venues_table.sql 
│   ├── 003_create_concerts_table.sql
│
├── concerts.db             
├── main.py                  
└── README.md               
Database Design
The project uses an SQLite database called concerts.db that contains three main tables: bands, venues, and concerts. Below are the details of these tables:

Bands Table
Stores information about the bands.

Column	Type	Description
id	INT	Primary key (auto-incremented)
name	TEXT	Name of the band
hometown	TEXT	Hometown of the band
Venues Table
Stores information about the venues.

Column	Type	Description
id	INT	Primary key (auto-incremented)
title	TEXT	Name of the venue
city	TEXT	City where the venue is located
Concerts Table
Stores information about the concerts, including which band is performing at which venue and on which date.

Column	Type	Description
id	INT	Primary key (auto-incremented)
date	TEXT	Date of the concert
band_id	INT	Foreign key (references bands(id))
venue_id	INT	Foreign key (references venues(id))
Database Interactions
Inserting Data
You can manually insert data into the database tables. Here's how the data is structured:

Insert a band into the bands table:                                             INSERT INTO bands (name, hometown) VALUES ('The Beatles', 'Liverpool');
INSERT INTO bands (name, hometown) VALUES ('Wakadinali', 'Nairobi');

Insert a venue into the venues table:
INSERT INTO venues (title, city) VALUES ('Wembley Stadium', 'London');
INSERT INTO venues (title, city) VALUES ('Uhuru Gardens', 'Nairobi');

Insert a concert linking a band and a venue:
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-07-15', 1, 1);

Querying Data
Retrieving all bands:                                                           SELECT * FROM bands;
Output:                                                                         1 | The Beatles | Liverpool
2 | Wakadinali  | Nairobi

Retrieving all venues:                                                          SELECT * FROM venues;
Output:
1 | Wembley Stadium | London
2 | Uhuru Gardens   | Nairobi

Retrieving concerts:
SELECT * FROM concerts;
Output:
1 | 2024-07-15 | 1 | 1
2 | 2024-07-15 | 1 | 1

Updating Data
You can update data in the database if necessary. For example, fixing a typo in a venue’s city name:
UPDATE venues 
SET city = 'Nairobi'
WHERE city = 'Nairibi';

Main Functionalities
Band Class
The Band class encapsulates the logic for band-related operations. Key methods include:

find(band_id): Finds a band by ID.
concerts(): Retrieves all concerts the band is performing in.
venues(): Retrieves all venues the band has performed at.
play_in_venue(venue_title, date): Adds a new concert for the band at a specific venue.
all_introductions(): Generates an introduction message for each concert based on the band's hometown and venue.
Venue Class
The Venue class provides methods for venue-related operations. Key methods include:

find(venue_id): Finds a venue by ID.
concerts(): Retrieves all concerts happening at the venue.
bands(): Retrieves all bands that have performed at the venue.
most_frequent_band(): Finds the band that has performed most frequently at the venue.
Concert Class
The Concert class manages concert-related operations. Key methods include:

band(): Returns the band performing in the concert.
venue(): Returns the venue of the concert.
hometown_show(): Determines if the concert is a hometown show for the band.
introduction(): Generates a concert introduction based on the band and venue.
main.py Overview
The main.py file is the main entry point of the application. It demonstrates how the classes are used to:

Find a band and venue by ID.
Create a concert using the play_in_venue() method.
Retrieve and print the band's concerts.
Retrieve and print all bands that have performed at a specific venue.
Print an introduction for a concert.

Example output:                                                                 Band Concerts: [('2024-07-15', 'Wembley Stadium')]
Venue Bands: [('The Beatles', 'Liverpool')]
Hello London!!!!! We are The Beatles and we're from Liverpool

How to Run
Once the setup is complete, you can run the application by executing:           python main.py
This will execute the default functionality as defined in the main.py file, including creating concerts, retrieving band and venue data, and generating concert introductions.


