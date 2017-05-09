from clients.return_geocode import ReturnGeocode
from clients.return_places import ReturnPlaces
from clients.return_distance_matrix import ReturnDistanceMatrix
from clients.return_average_prices import ReturnAveragePrices

from constants import SAMPLE_DESTINATION, SAMPLE_ORIGIN, INTEREST_TYPES, DEFAULT_RADIUS, DEFAULT_MODES


class GetApartmentData:
    place = ReturnPlaces()
    geocode = ReturnGeocode()
    distance = ReturnDistanceMatrix()
    prices = ReturnAveragePrices()

    # get Google data from a given address
    def get_address_place(self, address):
        return self.place.search_place_nearby_query(address)

    def get_crime_rate(self, place_id):
        sector = self.geocode.return_sector(place_id)
        return self.geocode.return_district_crime_rate(2016, sector)

    def get_interest_points(self, location, radius, type):
        return self.place.search_place_nearby(location=location, radius=radius, type=type)

    def get_me_data(self):
        # TODO: remove [1]
        for address in [SAMPLE_ORIGIN[1]]:
            print ">>>>>>><<<<<<<<<"
            place = self.get_address_place(address)
            print "Address: %s" % address
            print "Crime rate:%s" % self.get_crime_rate(place['place_id'])

            for interest in [INTEREST_TYPES[0]]:
                interest_points = self.get_interest_points(place['geometry']['location'], DEFAULT_RADIUS, interest)
                # Returns {'duration': u'8 mins', 'place_id': u'ChIJsfavwjYAskAR6pGbD04Vcoc'}
                closest = self.distance.getTheClosestPlace(address, interest_points.keys())
                print u''+ "Closest %s type for %s is %s at %s distance." \
                           % (interest, address, interest_points[closest['place_id']].encode('ascii','replace'), closest['duration'])

            destinations_matrix = self.distance.getAllModesMatrix(address, SAMPLE_DESTINATION)

            for destination in destinations_matrix:
                print "Distances and Duration time for %s" % (destination['name'])
                for mode in destination['modes']:
                    if destination['modes'][mode]:
                        print "   %s: duration %s , distance %s" % (mode, destination['modes'][mode]['duration']['text'], destination['modes'][mode]['distance']['text'])

            avg_price = self.prices.return_average_price(self.geocode.return_sector(place['place_id']))
            print "Average price in the area is %s EURO/sqm" % avg_price


# RUN
print "Entered here"
apt = GetApartmentData()
apt.get_me_data()

