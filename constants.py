# Bucharest center
BUCHAREST = (44.439, 26.096)

GEOCODE_KEY = 'AIzaSyADavpMHJIkaddSzElHqIFRfTqGs4uWkYc'
PLACES_KEY = 'AIzaSyBQQr8KkPsUE-QA4wEw_zlKa7oKNZVviQY'
MATRIX_KEY = 'AIzaSyDZBy-kV9lX5z8XHZjKyTG4y6h0kyIxD6E'

SAMPLE_ORIGIN = ["The Park appartments","Global City Residence","Iuliu Maniu 94-100"]
SAMPLE_DESTINATION = ["Strada Mr. Campeanu Alexandru 24"]

SAMPLE_PLACE_ID = ["ChIJKY2Wd2oCskARMfjunqzJVHU","ChIJwSjue0L_sUAR3K2rAviJECs"]

default_modes = ["walking","driving","bicycling","transit"]

query_items = [
    {
        'query': 'unirii',
        'location': BUCHAREST,
        'radius': 2000,
        'type': 'subway_station'
    },
    {
        'query': '',
        'location': BUCHAREST,
        'radius': 2000,
        'type': 'parking'
    },
    {
        'query': 'AFI',
        'location': BUCHAREST,
        'radius': 2000,
        'type': 'shopping_mall'
    },
    {
        'query': '',
        'location': BUCHAREST,
        'radius': 2000,
        'type': 'school'
    },
    {
        'query': 'Herastrau',
        'location': BUCHAREST,
        'radius': 2000,
        'type': 'park'
    }
]