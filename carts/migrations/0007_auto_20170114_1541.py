# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20170112_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=25.0, null=True, max_digits=50, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=25.0, null=True, max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(default=25.0, null=True, max_digits=50, decimal_places=2),
        ),
    ]
