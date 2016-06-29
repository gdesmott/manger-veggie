# -*- coding: utf-8 -*-
from settings import *

INSTALLED_APPS = ( 'vegoresto',  ) + INSTALLED_APPS

JSTEMPLATE_DIRS.append(os.path.join(BASE_DIR, 'vegoresto', 'templates'))

VEGO_RESTO = True
APP_NAME = "VegOresto"

LEAFLET_CONFIG['DEFAULT_CENTER'] = (46.9, 2.791)
LEAFLET_CONFIG['DEFAULT_ZOOM'] = 6
LEAFLET_CONFIG['MIN_ZOOM'] = 6

# LEAFLET_CONFIG['TILES'] = "xxx" # in case of API key/URL override

