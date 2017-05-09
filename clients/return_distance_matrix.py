import googlemaps
from constants import DEFAULT_MODES, MATRIX_KEY

class ReturnDistanceMatrix:
    def __init__(self):
        self.client = googlemaps.Client(MATRIX_KEY)

    def getMatrix(self,origins,destinations,mode=None):
        combinations = len(origins) * len(destinations)
        if (not isinstance(origins, str)) and combinations >100:
            raise Exception("Too much combination : " + str(combinations))
        return self.client.distance_matrix(origins,destinations,mode)

    def getAllModesMatrix(self,origin,destinations):
        matrix = {}
        for mode in DEFAULT_MODES:
            matrix[mode] = self.getMatrix(origin,destinations,mode)

        destinations_matrix = []
        counter = 0
        for destination in destinations:
            destinations_matrix_element = {}
            destinations_matrix_element["name"] = destination
            modes_elements = {}
            for mode in DEFAULT_MODES:
                modes_elements[mode] = {}
                if matrix[mode]['status'] == 'OK' and matrix[mode]['rows'][0]['elements'][counter]['status'] == 'OK':

                    modes_elements[mode]['duration'] = matrix[mode]['rows'][0]['elements'][counter]['duration']
                    modes_elements[mode]['distance'] = matrix[mode]['rows'][0]['elements'][counter]['distance']
            counter+=1
            destinations_matrix_element['modes'] = modes_elements
            destinations_matrix.append(destinations_matrix_element)
            # address, mode, distance, duration

        return destinations_matrix

    def getTheClosestPlace(self,origin,places):
        destinations = []
        for place in places:
            destinations.append('place_id:'+place)
        matrix = self.getMatrix(origin,destinations)
        min_distance= None
        min_distance_string = ""
        iterator = 0
        winner = 0
        for row in matrix['rows']:
            for place in row['elements']:
                if place['status'] == 'OK' and (min_distance is None or min_distance > place['duration']['value']) :
                    min_distance = place['duration']['value']
                    min_distance_string= place['duration']['text']
                    winner = iterator
                iterator+=1
        response = {}
        response['place_id'] = places[winner]
        response['duration'] = min_distance_string
        return response
