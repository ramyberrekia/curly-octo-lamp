# Generated by Django 3.2 on 2022-06-01 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotelimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='context',
            new_name='content',
        ),
    ]