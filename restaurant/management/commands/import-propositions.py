# -*- coding: utf-8 -*-
import csv

from django.core.management.base import BaseCommand
from django.db import transaction

from restaurant.models import Restaurant


class Command(BaseCommand):
    args = '<csv-file>'

    def handle(self, *args, **options):
        with transaction.atomic():
            Restaurant.objects.all().delete()

            with open(args[0], 'rb') as csvfile:
                reader = csv.DictReader(csvfile)

                for fake_id, row in enumerate(reader, 1):
                    if not row['Nom du restaurant']:
                        continue

                    print row['Nom du restaurant']
                    restaurant = Restaurant.create(
                        vegoresto_id=fake_id,
                        name=row['Nom du restaurant'].decode("Utf-8"),
                        address=row['Adresse compl\xc3\xa8te'].decode("Utf-8"),
                        website=row['Site web'].decode("Utf-8"),
                        contact=row['Votre email'].decode("Utf-8"),
                    )

                    restaurant.active = True
                    review = row['Plat v\xc3\xa9g\xc3\xa9tarien/v\xc3\xa9g\xc3\xa9talien que vous avez mang\xc3\xa9']
                    if len(review) < 10:
                        restaurant.review = "Il n'y a pas eu d'informations données par la personne ayant soumis le restaurant."
                    else:
                        restaurant.review = review

                    restaurant.save()
