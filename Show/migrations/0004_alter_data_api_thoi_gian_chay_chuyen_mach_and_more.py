# Generated by Django 4.2.8 on 2023-12-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0003_data_api_hieusuat_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_api',
            name='Thoi_Gian_Chay_Chuyen_Mach',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='data_api',
            name='Thoi_Gian_Tat_Chuyen_Mach',
            field=models.TimeField(auto_now=True),
        ),
    ]
