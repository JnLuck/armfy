# Generated by Django 5.1.1 on 2024-09-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_profilesteel_name_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilesteel',
            name='name_origin',
            field=models.CharField(default='Nullmx', max_length=300, unique=True),
        ),
    ]