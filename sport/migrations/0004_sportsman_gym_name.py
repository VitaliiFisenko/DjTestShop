# Generated by Django 2.2.6 on 2019-10-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0003_remove_sportsman_gym_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsman',
            name='gym_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
