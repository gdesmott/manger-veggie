from django.db import models

from taggit.managers import TaggableManager

import phonenumbers
from geopy.geocoders import ArcGIS, OpenMapQuest, GoogleV3, Nominatim, GeocoderDotUS

GEOCODERS = [Nominatim, GoogleV3, ArcGIS, OpenMapQuest, GeocoderDotUS]


class Restaurant(models.Model):


    vegoresto_id = models.BigIntegerField(unique=True)

    review = models.TextField(null=True)
    approved_date = models.DateField(null=True)

    description = models.TextField(null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    main_image = models.URLField(null=True)

    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    tags = TaggableManager()

    TODO = 'TODO'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    STATUS_CHOICES = (
        (TODO, 'TODO'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=TODO)

    # admin
    checked = models.BooleanField(default=False)
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

        restaurant.update_checked()
        return restaurant

    def should_be_checked(self):
        if self.status is None or 'OK' not in self.status:
            return False

        return True

    def update_checked(self):
        self.checked = self.should_be_checked()
        self.save()

    def get_national_phone_number(self):
        if self.phone is None:
            return None

        # FIXME: don't assume the restaurant is in Belgium
        x = phonenumbers.parse(self.phone, "BE")
        return phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)

    def get_international_phone_number(self):
        if self.phone is None:
            return None

        # FIXME: don't assume the restaurant is in Belgium
        x = phonenumbers.parse(self.phone, "BE")
        return phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)

    def tags_for_js(self):
        return [x.name.encode("Utf-8") for x in self.tags.all()]

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
