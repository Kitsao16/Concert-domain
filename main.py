from models.band import Band
from models.venue import Venue
from models.concert import Concert


def main():
    # Example usage
    band = Band.find(1)  # Assuming the band with ID 1 exists
    venue = Venue.find(1)  # Assuming the venue with ID 1 exists

    # Create a concert
    band.play_in_venue("Wembley Stadium", "2024-07-15")

    # Get band concerts
    concerts = band.concerts()
    print("Band Concerts:", concerts)

    # Get venue bands
    venue_bands = venue.bands()
    print("Venue Bands:", venue_bands)

    # Get concert details
    concert = Concert(1, "2024-07-15", band.id, venue.id)
    print(concert.introduction())


if __name__ == "__main__":
    main()
