# Generated by Django 2.2.3 on 2019-08-16 12:06

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190816_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritething',
            name='audit_logs',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalfavoritething',
            name='audit_logs',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
    ]
