# Generated by Django 2.2.2 on 2021-02-24 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
    ]
