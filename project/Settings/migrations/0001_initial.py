# Generated by Django 3.2 on 2022-05-30 16:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='siteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/')),
                ('site_name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('description', models.TextField(max_length=150)),
                ('instagram_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('twitter_url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
    ]
