import json
from django.http import HttpResponse

from .models import Restaurant


def restaurants_json(request):
    return HttpResponse(json.dumps(list(Restaurant.objects.all().values("lat", "lon"))))
