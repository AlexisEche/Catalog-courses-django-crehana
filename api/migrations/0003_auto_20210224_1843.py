# Generated by Django 2.2.2 on 2021-02-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_course_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='real_price',
            field=models.FloatField(default=5),
        ),
    ]
