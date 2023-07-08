# Generated by Django 4.2.1 on 2023-07-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketer', '0003_marketer_createddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketer',
            old_name='house',
            new_name='houseId',
        ),
        migrations.AddField(
            model_name='marketer',
            name='min_amount',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=7),
        ),
    ]
