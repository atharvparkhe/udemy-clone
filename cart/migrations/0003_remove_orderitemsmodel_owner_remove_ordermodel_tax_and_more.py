# Generated by Django 4.0.2 on 2022-03-14 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_wishlistmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemsmodel',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='total_amt',
        ),
    ]
