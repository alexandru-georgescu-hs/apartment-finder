import googlemaps
from constants import GEOCODE_KEY, CRIME_RATE_BUCHAREST


class ReturnGeocode():
    """
    This function returns the Sector in which a place_id is located in Bucharest or any other city
    """
    # TODO: to test this on other cities as well
    gmaps = googlemaps.Client(key=GEOCODE_KEY)
    def return_sector(self, place_id):
        result = self.gmaps.reverse_geocode(latlng=place_id)
        return result[0]['address_components'][1]['short_name'].split()[-1]

    def return_district_crime_rate(self, year, sector):
        # Returns the crime rate based on year/sector
        if year not in [2014, 2015, 2016]:
            raise Exception('No crime data for the requested year.')
        return CRIME_RATE_BUCHAREST[str(year)][sector]
