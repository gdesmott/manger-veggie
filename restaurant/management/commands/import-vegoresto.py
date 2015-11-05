import HTMLParser
from django.core.management.base import BaseCommand

from restaurant.models import Restaurant
from BeautifulSoup import BeautifulSoup
import urllib2
from dateutil.parser import parse

from django.db import transaction

source_url = 'http://vegoresto.fr/restos-fichier-xml/'

VEGAN_FRIENDLY = 'vegan-friendly'

VG_TAGS = {
    'sans_gluten': 'gluten-free',
    'vege': 'vegetarian',
    'vegan': 'vegan',
    'vegan_friendly': VEGAN_FRIENDLY
}


def parse_vg_tags(tags):
    result = set()

    for t in filter(None, map(lambda x: x.strip(), tags.split('|'))):
        try:
            result.add(VG_TAGS[t])
        except KeyError:
            print "WARNING: Unknown tag %s" % t

    return result


def unescape(string):
    string = HTMLParser.HTMLParser().unescape(string)
    return string


class Command(BaseCommand):
    args = ''

    def handle(self, *args, **options):

        s = urllib2.urlopen(source_url)
        xml_content = s.read()
        soup = BeautifulSoup(xml_content)

        with transaction.atomic():
            # hide everything, then we'll set restaurant with a
            # review as active later
            Restaurant.objects.update(active=False)

            for resto_data in soup.root.findAll('item'):
                vegoresto_id = int(resto_data.id.text)
                resto_set = Restaurant.objects.filter(vegoresto_id=vegoresto_id)
                name = resto_data.titre.text
                print 'importing {0}'.format(name.encode('utf-8'))

                if resto_set.exists():
                    resto = resto_set[0]
                    resto.name = unescape(unescape(name))
                    resto.address = unescape(resto_data.adresse.text)
                else:
                    resto = Restaurant.create(vegoresto_id=vegoresto_id,
                                              name=unescape(unescape(name)),
                                              address=unescape(resto_data.adresse.text))

                resto.active = True

                resto.review = unescape(resto_data.vegetik_review.text)
                resto.approved_date = parse(resto_data.vegetik_approved_date.text)
                resto.lat = float(resto_data.lat.text)
                resto.lon = float(resto_data.lon.text)
                resto.website = resto_data.site_internet.text
                resto.description = resto_data.description.text
                resto.phone = resto_data.tel_fixe.text
                resto.mail = resto_data.mel_public.text
                resto.main_image = resto_data.image.text
                resto.country_code = resto_data.pays.text.upper()
                resto.vegoresto_url = resto_data.vego_url.text
                if resto_data.vegoresto.text == '1':
                    resto.vegoresto = True

                tags = parse_vg_tags(resto_data.categories_culinaires.text)
                if resto_data.vegetik_veganfriendly.text == 'TRUE':
                    tags.add(VEGAN_FRIENDLY)
                if tags:
                    resto.tags.add(*tags)

                resto.save()
