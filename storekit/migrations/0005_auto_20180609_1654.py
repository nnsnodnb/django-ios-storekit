# Generated by Django 2.0.4 on 2018-06-09 16:54

from django.db import migrations

import storekit.fields


class Migration(migrations.Migration):

    dependencies = [
        ('storekit', '0004_auto_20180605_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inapp',
            name='original_transaction_id',
            field=storekit.fields.PositiveBigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='inapp',
            name='transaction_id',
            field=storekit.fields.PositiveBigIntegerField(blank=True),
        ),
    ]
