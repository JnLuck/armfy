# Generated by Django 5.1.1 on 2024-10-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledetail',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
