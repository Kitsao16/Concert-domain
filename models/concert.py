from models.band import Band
from models.venue import Venue


class Concert:
    def __init__(self, concert_id, date, band_id, venue_id):
        self.id = concert_id
        self.date = date
        self.band_id = band_id
        self.venue_id = venue_id

    def band(self):
        return Band.find(self.band_id)

    def venue(self):
        return Venue.find(self.venue_id)

    def hometown_show(self):
        band = self.band()
        venue = self.venue()
        return band.hometown == venue.city

    def introduction(self):
        band = self.band()
        venue = self.venue()
        return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"
