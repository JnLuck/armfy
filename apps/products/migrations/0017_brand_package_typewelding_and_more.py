# Generated by Django 5.1.1 on 2024-11-06 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_delete_productprofilesteel_delete_productwelding_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkg_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='TypeWelding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tw_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'TypeWelding',
                'verbose_name_plural': 'TypeWeldings',
            },
        ),
        migrations.RemoveField(
            model_name='welding',
            name='name_welding',
        ),
        migrations.AddField(
            model_name='welding',
            name='thickness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='welds_thickness', to='products.thickness'),
        ),
        migrations.AddField(
            model_name='welding',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='welds_brand', to='products.brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='welding',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='welds_package', to='products.package'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='welding',
            name='type_welding',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='welds_tw', to='products.typewelding'),
            preserve_default=False,
        ),
    ]
