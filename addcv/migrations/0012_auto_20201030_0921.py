# Generated by Django 3.0.6 on 2020-10-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcv', '0011_auto_20201030_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='temp_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
