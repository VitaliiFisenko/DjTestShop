# Generated by Django 2.2.6 on 2019-10-28 12:39

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_remove_myfields_custom_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfields',
            name='date_now',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='field_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='field_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='field_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, message="Price can't be less than 0")]),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='field_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='field_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message="Year can't be less than 0")]),
        ),
        migrations.AlterField(
            model_name='myfields',
            name='is_superfield',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
    ]
