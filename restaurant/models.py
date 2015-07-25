from django.db import models
from django.conf import settings

from taggit.managers import TaggableManager

import phonenumbers
from geopy.geocoders import ArcGIS, OpenMapQuest, GoogleV3, Nominatim, GeocoderDotUS

GEOCODERS = [Nominatim, GoogleV3, ArcGIS, OpenMapQuest, GeocoderDotUS]

VEGO_RESTO_URL = "http://vegoresto.fr/resto/%s"

class Restaurant(models.Model):
    vegoresto_id = models.BigIntegerField(unique=True)
    vegoresto_url = models.TextField(null=True)

    active = models.BooleanField(default=False)

    review = models.TextField(null=True)
    approved_date = models.DateField(null=True)

    description = models.TextField(null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=2, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    main_image = models.URLField(null=True)

    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    tags = TaggableManager()

    # admin
    contact = models.CharField(max_length=255, null=True, blank=True)
    vg_contact = models.CharField(max_length=255, null=True, blank=True)

    @classmethod
    def create(cls, vegoresto_id, name, address, website=None, phone=None, mail=None, contact=None, vg_contact=None):
        if website is not None and not website.startswith('http'):
            website = 'http://%s' % website

        restaurant = cls.objects.create(vegoresto_id=vegoresto_id, name=name, address=address, website=website,
                phone=phone, mail=mail, contact=contact, vg_contact=vg_contact)
        print "added:", name

        for geo in GEOCODERS:
            geolocator = geo()
            try:
                location = geolocator.geocode(address)
            except:
                continue

            if location is not None:
                break

        if location is not None:
            restaurant.lat = location.latitude
            restaurant.lon = location.longitude
            restaurant.save()
        else:
            print "Unknown address: %s (%s)" % (address, name)

        return restaurant

    def _parse_phone_number(self):
        if self.phone is None:
            return None

        try:
            return phonenumbers.parse(self.phone, self.country_code)
        except phonenumbers.NumberParseException:
            print "Warning: '%s' is an uparsable phone number" % self.phone
            return None

    def get_national_phone_number(self):
        phone_number = self._parse_phone_number()

        if phone_number is None:
            return None

        return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)

    def get_international_phone_number(self):
        phone_number = self._parse_phone_number()

        if phone_number is None:
            return None

        return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)

    def get_details_page(self):
        if settings.VEGO_RESTO:
            return VEGO_RESTO_URL % self.vegoresto_url

        return 'restaurant/%s' % self.id

    def tags_for_js(self):
        return [x.name.encode("Utf-8") for x in self.tags.all()]

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
