# Generated by Django 2.2 on 2019-04-13 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190412_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='title',
        ),
    ]
