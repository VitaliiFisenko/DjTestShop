# Generated by Django 2.2.6 on 2019-10-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_sportsman_gym_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsman',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
