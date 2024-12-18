# Generated by Django 5.1.1 on 2024-11-18 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_numerationvoucher_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='numeration_voucher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sales_numeration_voucher', to='sales.numerationvoucher'),
            preserve_default=False,
        ),
    ]
