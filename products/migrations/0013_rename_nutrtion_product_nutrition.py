# Generated by Django 3.2.6 on 2021-08-13 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_allergy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nutrtion',
            new_name='nutrition',
        ),
    ]
