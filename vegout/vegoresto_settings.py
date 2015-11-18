# -*- coding: utf-8 -*-
from settings import *

VEGO_RESTO = True
APP_NAME = "VegOresto"

TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'restaurant', 'templates', 'vegoresto'))

LEAFLET_CONFIG['DEFAULT_CENTER'] = (46.464, 2.791)
LEAFLET_CONFIG['DEFAULT_ZOOM'] = 7

# LEAFLET_CONFIG['TILES'] = "xxx" # in case of API key/URL override

