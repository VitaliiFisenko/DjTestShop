# Generated by Django 2.2.6 on 2019-10-25 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfields',
            name='custom_date',
        ),
    ]
