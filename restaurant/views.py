import json
from django.http import HttpResponse
from django.conf import settings

from .models import Restaurant

# Vegetik review minimal length
MIN_REVIEW_LEN = 10

def restaurants_json(request):
    # Filter the restaurant to display on the map
    f = { 'lat__isnull': False,
          'lon__isnull': False,
          'active': True }

    if settings.VEGO_RESTO:
        # TODO: how do we want to filter vego resto restaurants?
        pass
    else:
        f['review__iregex'] = r'^.{%d,}$' % MIN_REVIEW_LEN

    return HttpResponse(json.dumps([{
        "lat": x.lat,
        "lon": x.lon,
        "name": x.name,
        "address": x.address,
        "website": x.website,
        "phone": x.phone,
        "id": x.id,
        "national_phone_number": x.get_national_phone_number(),
        "international_phone_number": x.get_international_phone_number(),
        "details_page": x.get_details_page(),
        "tags": [tag["name"] for tag in x.tags.all().values("name")],
    } for x in Restaurant.objects.filter(**f)], indent=4))

    # optimisation note: .prefetch_related("tags") makes request slower here
