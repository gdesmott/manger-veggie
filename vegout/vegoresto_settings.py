from settings import *

VEGO_RESTO = True
APP_NAME = "Vego Resto"

TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'restaurant', 'templates', 'vegoresto'))
