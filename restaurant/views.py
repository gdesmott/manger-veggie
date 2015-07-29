import json
from django.http import HttpResponse

from .models import Restaurant
from .utils import VG_TAGS


def restaurants_json(request):
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
        "tags": [tag["name"] for tag in x.tags.all().values("name") if tag["name"] in VG_TAGS.values()],
        "other_tags": [tag["name"] for tag in x.tags.all().values("name") if tag["name"] not in VG_TAGS.values()],
    } for x in Restaurant.objects.filter(lat__isnull=False, lon__isnull=False, active=True)], indent=4))

    # optimisation note: .prefetch_related("tags") makes request slower here
