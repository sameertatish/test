# Generated by Django 4.2.1 on 2023-07-07 18:14

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_house_avaliableforsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOperations',
            fields=[
                ('marketerCommission', models.BooleanField(auto_created=True, default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('houseId', models.UUIDField(default=uuid.uuid4)),
                ('marketerId', models.UUIDField(default=uuid.uuid4)),
                ('priceHouse', models.DecimalField(decimal_places=2, max_digits=6)),
                ('createdDate', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='createdDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
