from clients.return_geocode import ReturnGeocode
from clients.return_places import ReturnPlaces
from clients.return_distance_matrix import ReturnDistanceMatrix
from clients.return_average_prices import ReturnAveragePrices
from clients.input_data import InputData

from constants import SAMPLE_DESTINATION, SAMPLE_ORIGIN, INTEREST_TYPES, DEFAULT_RADIUS, DEFAULT_MODES


class GetApartmentData:
    place = ReturnPlaces()
    geocode = ReturnGeocode()
    distance = ReturnDistanceMatrix()
    prices = ReturnAveragePrices()
    input_data = InputData()
    possible_addresses = []
    possible_interests = []

    # get Google data from a given address
    def get_address_place(self, address):
        return self.place.search_place_nearby_query(address)

    def get_crime_rate(self, place_id):
        sector = self.geocode.return_sector(place_id)
        rate_percentage = self.geocode.return_district_crime_rate(2016, sector)
        if rate_percentage <= 80:
            rate = "LOW"
        elif rate_percentage > 80 and rate_percentage < 100:
            rate = "MEDIUM"
        else:
            rate = "HIGH"
        return (rate, rate_percentage)

    def get_interest_points(self, location, radius, type):
        return self.place.search_place_nearby(location=location, radius=radius, type=type)

    def get_user_data(self):
        # Enter possible appartment places
        print "Please enter possible appartment places (max 3)"
        self.possible_addresses = self.input_data.get_address('\n    Address: ', 3)

        # Enter interest points
        print "\nPlease enter possible interest places (max 3)"
        self.possible_interests = self.input_data.get_address('\n    Address: ', 3)

        # TODO: Enter interest types
        # print "\n Coose from the following interest types: "
        # print INTEREST_TYPES


    def get_me_data(self):
        #TODO: add data
        defaults = raw_input('Use default data?  (y/n): ')
        if defaults.lower() == 'n':
            self.get_user_data()
        else:
            print "    using defaults..."
            print "\nPossible appartments:"
            print SAMPLE_ORIGIN
            self.possible_addresses = SAMPLE_ORIGIN

            print "\nInterest points:"
            print SAMPLE_DESTINATION
            self.possible_interests = SAMPLE_DESTINATION

        for address in self.possible_addresses:
            place = self.get_address_place(address)
            print "\n============ Here is the data we could find for %s ============" % address
            # print "\nAddress: %s " % address
            destinations_matrix = self.distance.getAllModesMatrix(address, self.possible_interests)
            for destination in destinations_matrix:
                print "Distances and Duration time for %s" % (destination['name'])
                for mode in destination['modes']:
                    if destination['modes'][mode]:
                        print "   %s: duration %s , distance %s" % \
                              (mode, destination['modes'][mode]['duration']['text'], destination['modes'][mode]['distance']['text'])

            for interest in INTEREST_TYPES:
                interest_points = self.get_interest_points(place['geometry']['location'], DEFAULT_RADIUS, interest)
                # Returns {'duration': u'8 mins', 'place_id': u'ChIJsfavwjYAskAR6pGbD04Vcoc'}
                closest = self.distance.getTheClosestPlace(address, interest_points.keys())
                print u''+ "Closest %s is:   %s at %s driving." \
                           % (interest, interest_points[closest['place_id']].encode('ascii','replace'), closest['duration'])

            avg_price = self.prices.return_average_price(self.geocode.return_sector(place['place_id']))
            print "Average price in the area is %s EURO/sqm" % avg_price
            print "Crime rated as %s with and index of %s according to 2016 stats." % self.get_crime_rate(place['place_id'])


# RUN
apt = GetApartmentData()
apt.get_me_data()

