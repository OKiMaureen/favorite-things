# Generated by Django 2.2.3 on 2019-07-25 20:45

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190722_2025'),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='FavoriteThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('ranking', models.PositiveIntegerField()),
                ('metadata', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
            options={
                'db_table': 'core_favorite_thing',
            },
        ),
        migrations.AddConstraint(
            model_name='favoritething',
            constraint=models.UniqueConstraint(fields=('title', 'category'), name='unique_favorite_thing'),
        ),
    ]