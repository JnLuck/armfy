# Generated by Django 5.1.1 on 2024-09-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_measure', models.CharField(max_length=255)),
                ('abbreviation_measure', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Measure',
                'verbose_name_plural': 'Measures',
            },
        ),
    ]
