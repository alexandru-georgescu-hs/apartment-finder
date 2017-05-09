# Bucharest center
BUCHAREST = (44.439, 26.096)

GEOCODE_KEY = 'AIzaSyADavpMHJIkaddSzElHqIFRfTqGs4uWkYc'
PLACES_KEY = 'AIzaSyAOQIfeLkOkmbwRlf395wFOYweHMomxTHg'
MATRIX_KEY = 'AIzaSyDZBy-kV9lX5z8XHZjKyTG4y6h0kyIxD6E'

SAMPLE_ORIGIN = ["The Park appartments Bucharest","Global City Residence Bucharest","Iuliu Maniu 94-100 Bucharest"]
SAMPLE_DESTINATION = ["Strada Mr. Campeanu Alexandru 24", "Iolanda Balas Bucharest", "Piata Unirii Bucharest"]

SAMPLE_PLACE_ID = ["ChIJKY2Wd2oCskARMfjunqzJVHU","ChIJwSjue0L_sUAR3K2rAviJECs"]

INTEREST_TYPES = ["park", "subway_station", "shopping_mall"]

DEFAULT_RADIUS = 3000

DEFAULT_MODES = ["walking", "driving", "bicycling", "transit"]

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


CRIME_RATE_BUCHAREST = {
    '2014': {
        '1': 93.36,
        '2': 84.85,
        '3': 129.53,
        '4': 121.23,
        '5': 61.13,
        '6': 109.94,
    },
    '2015': {
        '1': 91.89,
        '2': 99.72,
        '3': 124.69,
        '4': 117.96,
        '5': 61.21,
        '6': 104.50,
    },
    '2016': {
        '1': 109.11,
        '2': 104.06,
        '3': 108.03,
        '4': 103.70,
        '5': 68.68,
        '6': 106.40,
    }
}