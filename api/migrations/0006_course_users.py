# Generated by Django 2.2.2 on 2021-02-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.IntegerField(default=0),
        ),
    ]
