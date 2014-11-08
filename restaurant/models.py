from django.db import models

from geopy.geocoders import ArcGIS, OpenMapQuest, GoogleV3, Nominatim, GeocoderDotUS

GEOCODERS = [Nominatim, GoogleV3, ArcGIS, OpenMapQuest, GeocoderDotUS]

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)

    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    # admin
    contact = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    vg_contact = models.CharField(max_length=255, null=True, blank=True)

    @classmethod
    def create(cls, name, address, website=None, phone=None, mail=None, contact=None, status=None, vg_contact=None):
        if website is not None and not website.startswith('http'):
            website = 'http://%s' % website

        restaurant = cls.objects.create(name=name, address=address, website=website,
                phone=phone, mail=mail, contact=contact, status=status, vg_contact=vg_contact)
        print "added:", name

        for geo in GEOCODERS:
            geolocator = geo()
            location = geolocator.geocode(address)
            if location is not None:
                break

        if location is not None:
            restaurant.lat = location.latitude
            restaurant.lon = location.longitude
            restaurant.save()
        else:
            print "Unknown address: %s (%s)" % (address, name)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
