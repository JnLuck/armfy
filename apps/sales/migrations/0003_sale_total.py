# Generated by Django 5.1.1 on 2024-10-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_saledetail_sub_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='total',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=10),
            preserve_default=False,
        ),
    ]
