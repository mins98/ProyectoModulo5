# Generated by Django 4.1.1 on 2022-10-04 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_alter_biblioteca_numerotelefonico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fechaPrestamo',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 21, 47, 12, 413716)),
        ),
    ]
