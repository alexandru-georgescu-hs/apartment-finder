from clients.return_geocode import ReturnGeocode


# This file returns the sector for a place_id which can be get using get_places.py function
client = ReturnGeocode()
place_id = 'ChIJ8egJWkn_sUART1OVw-Irz80'

print client.return_sector(place_id=place_id)
