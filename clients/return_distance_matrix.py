import googlemaps
from constants import default_modes, MATRIX_KEY

class ReturnDistanceMatrix:
    def __init__(self):
        self.client = googlemaps.Client(MATRIX_KEY)

    def getMatrix(self,origins,destinations,mode=None):
        combinations = len(origins) * len(destinations)
        if combinations >100:
            raise Exception("Too much combination : " + str(combinations))
        return self.client.distance_matrix(origins,destinations,mode)

    def getAllModesMatrix(self,origin,destinations):
        matrix = {}
        for mode in default_modes:
            matrix[mode] = self.getMatrix(origin,destinations,mode)
        return matrix

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
