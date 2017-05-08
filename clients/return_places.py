import googlemaps
from constants import PLACES_KEY


class ReturnPlaces():
    # Use Places api:
    # https://github.com/googlemaps/google-maps-services-python/blob/master/googlemaps/places.py

    gmaps = googlemaps.Client(key=PLACES_KEY)
    def search_place_nearby_id(self, location, radius, type):
        """
        returns a list of dictionaries containing 'location' coordinates and the 'id' for a location
        """
        places = []
        result = self.gmaps.places_nearby(location=location, radius=radius, type=type)

        for item in result['results']:
            places.append(item['place_id'])
        return places

    def search_place_nearby(self, location, radius, type):
        """
        returns a list of dictionaries containing 'location' coordinates and the 'id' for a location
        """
        places = []
        result = self.gmaps.places_nearby(location=location, radius=radius, type=type)
        return result['results']

