# Generated by Django 5.1.1 on 2024-09-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_shape'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_steel', models.CharField(max_length=255)),
                ('abbreviation_steel', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Steel',
                'verbose_name_plural': 'Steels',
            },
        ),
    ]
