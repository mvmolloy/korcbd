# Generated by Django 3.1.1 on 2020-10-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201009_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_qty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]