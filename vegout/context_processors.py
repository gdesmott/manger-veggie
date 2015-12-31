from django.conf import settings

def flavour(request):
    return {'ANDROID_APP_URL': settings.ANDROID_APP_URL,
            'APP_NAME': settings.APP_NAME,
            'VEGO_RESTO': settings.VEGO_RESTO,
            'USE_PIWIK': settings.USE_PIWIK,
            }
