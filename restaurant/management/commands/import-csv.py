# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
#from optparse import make_option

import csv

from restaurant.models import Restaurant

MIN_FIELD_LEN = 3

class Command(BaseCommand):
    args = '<csv-file>'

    def handle(self, *args, **options):
        Restaurant.objects.all().delete()

        with open(args[0], 'rb') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # clean up
                for k, v in row.items():
                    if v == '?' or len(v) < MIN_FIELD_LEN:
                        # discard
                        row[k] = None
                        continue

                    if k == 'Mail' and '@' not in v:
                        row[k] = None
                        continue

                    row[k] = v.strip()

                if not row['Nom'] or not row['Adresse']:
                    continue

                if row['Suivi'] is None or 'OK' not in row['Suivi']:
                    continue

                Restaurant.create(row['Nom'], row['Adresse'], row['Site'], row['Téléphone'], row['Mail'], row['Personne de contact'], row['Suivi'], row['Personne responsable'])
