# Generated by Django 2.2.2 on 2021-02-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210228_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(default=5),
        ),
    ]