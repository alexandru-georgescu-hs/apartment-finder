from constants import BUCHAREST,SAMPLE_ORIGIN
from clients.return_places import ReturnPlaces

client = ReturnPlaces()
print client.search_place_nearby_id(SAMPLE_ORIGIN, 6000, 'park')

#To query an exact address
start_point = client.search_place_nearby_query('Iuliu Maniu 94-100')
print start_point

#nearby needs long and lat
print client.search_place_nearby(start_point, radius=4000, type='park')
