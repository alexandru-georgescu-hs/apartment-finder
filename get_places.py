from constants import BUCHAREST
from clients.return_places import ReturnPlaces

client = ReturnPlaces()
print client.search_place_nearby_id(BUCHAREST, 2000, 'park')

print "========================="
print client.search_place_nearby(BUCHAREST, 2000, 'park')