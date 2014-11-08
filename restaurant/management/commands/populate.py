# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
#from optparse import make_option

from restaurant.models import Restaurant

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
    )

    def create_restaurant(self, name, address, website=None, phone=None, mail=None, contact=None, status=None, vg_contact=None):
        if not website.startswith('http'):
            website = 'http://%s' % website

        Restaurant.objects.create(name=name, address=address, website=website,
                phone=phone, mail=mail, contact=contact, status=status, vg_contact=vg_contact)

    def handle(self, *args, **options):
        Restaurant.objects.all().delete()

        self.create_restaurant("Exki", "12, Chaussée D'Ixelles, 1050 Ixelles", 'www.exki.be', '02/502.72.77', status='2ème vague')
