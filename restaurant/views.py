import json
from django.http import HttpResponse

from .models import Restaurant


def restaurants_json(request):
    return HttpResponse(json.dumps([{
        "lat": x.lat,
        "lon": x.lon,
        "name": x.name,
        "address": x.address,
        "website": x.website,
        "phone": x.phone,
        "id": x.id,
    } for x in Restaurant.objects.filter(lat__isnull=False, lon__isnull=False, checked__exact=True)]))
