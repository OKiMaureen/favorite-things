# Generated by Django 2.2.3 on 2019-07-28 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190726_1302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoritething',
            options={'ordering': ['ranking']},
        ),
    ]
