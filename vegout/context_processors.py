from django.conf import settings

def flavour(request):
    return {'APP_NAME': settings.APP_NAME,
            'VEGO_RESTO': settings.VEGO_RESTO }
