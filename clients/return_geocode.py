import googlemaps
from constants import GEOCODE_KEY


class ReturnGeocode():
    """
    This function returns the Sector in which a place_id is located in Bucharest or any other city
    """
    # TODO: to test this on other cities as well
    gmaps = googlemaps.Client(key=GEOCODE_KEY)
    def return_sector(self, place_id):
        result = self.gmaps.reverse_geocode(latlng=place_id)
        return result[0]['address_components'][1]['short_name']
