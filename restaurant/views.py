import json
from django.http import HttpResponse

from .models import Restaurant


def restaurants_json(request):
    return HttpResponse(json.dumps(list(Restaurant.objects.filter(lat__isnull=False, lon__isnull=False).values("lat", "lon", "name", "address", "website", "phone", "id"))))
