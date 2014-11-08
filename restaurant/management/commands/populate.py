# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
#from optparse import make_option

from restaurant.models import Restaurant
from geopy.geocoders import Nominatim

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
    )

    def create_restaurant(self, name, address, website=None, phone=None, mail=None, contact=None, status=None, vg_contact=None):
        if website is not None and not website.startswith('http'):
            website = 'http://%s' % website

        restaurant = Restaurant.objects.create(name=name, address=address, website=website,
                phone=phone, mail=mail, contact=contact, status=status, vg_contact=vg_contact)
        print "added", name

        geolocator = Nominatim()
        location = geolocator.geocode(address)
        if location is not None:
            restaurant.lat = location.latitude
            restaurant.lon = location.longitude
            restaurant.save()
        else:
            print "Unknown address", address

    def handle(self, *args, **options):
        Restaurant.objects.all().delete()

        self.create_restaurant("Exki", "12, Chaussée D'Ixelles, 1050 Ixelles", 'www.exki.be', '02/502.72.77', status='2ème vague')
        self.create_restaurant("Ellis Gourmet Burger", "Place Sainte-Catherine, 4 - 1000 Bruxelles", "http://www.ellisgourmetburger.com/nl/", "02/514.23.14", status="OK (autocollant)", vg_contact="Lisa & Sophie - 28/06")
        self.create_restaurant("Den Teepot", "66, Rue des Chartreux 1000 Bruxelles", "http://www.bioshop.be/winkels/brussel.html", "02/511.94.02", status="OK (autocollant)", vg_contact="Lisa & Sophie - 28/06")
        self.create_restaurant("Toukoul", "34, Rue de Laeken 1000 Bruxelles ", "http://www.toukoul.be", "02/223.73.77", "info@toukoul.be", status="repasser à 13h", vg_contact="Lisa & Sophie - 28/06")
        self.create_restaurant("Mr Falafel", "53, Boulevard Lemonnier - 1000 Bruxelles", None, "0493/34.64.12", None, status="OK (autocollant)", vg_contact="Lisa & Sophie - 28/06")
        self.create_restaurant("Le Dolma", "329, Chaussée d'Ixelles - 1050 Ixelles", "www.dolma.be", "02/649.89.81", "info@dolma.be", status="OK (autocollant)", vg_contact="Lisa & Sophie H & Isabelle - 05/07")
