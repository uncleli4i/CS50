# Generated by Django 3.2.7 on 2021-11-24 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='os',
            name='revision',
        ),
    ]
