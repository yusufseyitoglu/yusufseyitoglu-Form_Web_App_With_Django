# Generated by Django 4.1.1 on 2022-10-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0016_alter_contactformmodel_rating1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating1',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='rating1'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='rating2'),
        ),
    ]
