from constants import SAMPLE_ORIGIN,SAMPLE_DESTINATION,SAMPLE_PLACE_ID
from clients.return_distance_matrix import ReturnDistanceMatrix

client = ReturnDistanceMatrix()
print "============getMatrix============="
print client.getMatrix(SAMPLE_ORIGIN,SAMPLE_DESTINATION)

print "============getAllModesMatrix============="
print client.getAllModesMatrix(SAMPLE_ORIGIN,SAMPLE_DESTINATION)

print "============getTheClosestPlace============="
print client.getTheClosestPlace('Iuliu Maniu 94-100',SAMPLE_PLACE_ID)