# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
#from optparse import make_option

from restaurant.models import Restaurant

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
    )

    def handle(self, *args, **options):
        Restaurant.objects.all().delete()

        Restaurant.create(1, "Exki", "12, Chaussée D'Ixelles, 1050 Ixelles", 'www.exki.be', '02/502.72.77', status='2ème vague')
        Restaurant.create(2, "Ellis Gourmet Burger", "Place Sainte-Catherine, 4 - 1000 Bruxelles", "http://www.ellisgourmetburger.com/nl/", "02/514.23.14", status="OK (autocollant)", vg_contact="Lisa & Sophie - 28/06")
        Restaurant.create(3, "Den Teepot", "66, Rue des Chartreux 1000 Bruxelles", "http://www.bioshop.be/winkels/brussel.html", "02/511.94.02", status="OK (autocollant)", vg_contact="Lisa & Sophie - 28/06")
        Restaurant.create(4, "Toukoul", "34, Rue de Laeken 1000 Bruxelles ", "http://www.toukoul.be", "02/223.73.77", "info@toukoul.be", status="repasser à 13h", vg_contact="Lisa & Sophie - 28/06")
        Restaurant.create(5, "Mr Falafel", "53, Boulevard Lemonnier - 1000 Bruxelles", None, "0493/34.64.12", None, status="OK (autocollant)", vg_contact="Lisa & Sophie - 28/06")
        Restaurant.create(6, "Le Dolma", "329, Chaussée d'Ixelles - 1050 Ixelles", "www.dolma.be", "02/649.89.81", "info@dolma.be", status="OK (autocollant)", vg_contact="Lisa & Sophie H & Isabelle - 05/07")
