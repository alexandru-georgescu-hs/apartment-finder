import googlemaps
from constants import BUCHAREST

gmaps = googlemaps.Client(key='AIzaSyBQQr8KkPsUE-QA4wEw_zlKa7oKNZVviQY')

class ReturnPlaces():
# Use Places api:
# https://github.com/googlemaps/google-maps-services-python/blob/master/googlemaps/places.py
    def search_place_nearby(self, location, radius, type):
        """
        returns a list of dictionaries containing 'location' coordinates and the 'id' for a location
        """
        places = []
        result = gmaps.places_nearby(location=location, radius=radius, type=type)

        # print type(places['results'])
        for item in result['results']:
            # places.append({'location': item['geometry']['location'], 'id': item['id']})
            places.append(item['place_id'])
        return places

# print search_place_nearby(query='herastrau', location=BUCHAREST, radius=2000, type='park')