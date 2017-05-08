import googlemaps


class ReturnPlaces():
    # Use Places api:
    # https://github.com/googlemaps/google-maps-services-python/blob/master/googlemaps/places.py

    gmaps = googlemaps.Client(key='AIzaSyBQQr8KkPsUE-QA4wEw_zlKa7oKNZVviQY')
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

