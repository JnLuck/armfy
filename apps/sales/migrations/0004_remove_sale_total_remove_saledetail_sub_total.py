# Generated by Django 5.1.1 on 2024-10-23 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_sale_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='total',
        ),
        migrations.RemoveField(
            model_name='saledetail',
            name='sub_total',
        ),
    ]
