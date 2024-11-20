# Generated by Django 5.1.1 on 2024-09-25 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_typeprofilesteel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileSteel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lengths_tps', to='products.length')),
                ('polygon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polygons_tps', to='products.polygon')),
                ('shape', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shapes_tps', to='products.shape')),
                ('steel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steels_tps', to='products.steel')),
                ('texture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='textures_tps', to='products.texture')),
                ('thickness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thickness_tps', to='products.thickness')),
                ('type_profile_steel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_steels_tps', to='products.typeprofilesteel')),
            ],
            options={
                'verbose_name': 'ProfileSteel',
                'verbose_name_plural': 'ProfileSteels',
            },
        ),
    ]