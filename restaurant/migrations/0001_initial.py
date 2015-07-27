# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vegoresto_id', models.BigIntegerField(unique=True)),
                ('active', models.BooleanField(default=True)),
                ('review', models.TextField(null=True)),
                ('approved_date', models.DateField(null=True)),
                ('description', models.TextField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('website', models.URLField(null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('country_code', models.CharField(max_length=2, null=True, blank=True)),
                ('mail', models.EmailField(max_length=254, null=True, blank=True)),
                ('main_image', models.URLField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('contact', models.CharField(max_length=255, null=True, blank=True)),
                ('vg_contact', models.CharField(max_length=255, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
