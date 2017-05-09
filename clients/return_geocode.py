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

        for item in result[0]['address_components']:
            if 'sector' in item['short_name'].lower():
                return item['short_name']
        return None


