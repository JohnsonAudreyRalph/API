# Generated by Django 4.2.8 on 2023-12-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0004_alter_data_api_thoi_gian_chay_chuyen_mach_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_API_read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vi_tri_1', models.IntegerField(blank=True, null=True)),
                ('vi_tri_2', models.IntegerField(blank=True, null=True)),
                ('vi_tri_3', models.IntegerField(blank=True, null=True)),
                ('vi_tri_4', models.IntegerField(blank=True, null=True)),
                ('vi_tri_5', models.IntegerField(blank=True, null=True)),
                ('vi_tri_6', models.IntegerField(blank=True, null=True)),
                ('vi_tri_7', models.IntegerField(blank=True, null=True)),
                ('vi_tri_8', models.IntegerField(blank=True, null=True)),
                ('vi_tri_9', models.IntegerField(blank=True, null=True)),
                ('vi_tri_10', models.IntegerField(blank=True, null=True)),
                ('vi_tri_11', models.IntegerField(blank=True, null=True)),
                ('vi_tri_12', models.IntegerField(blank=True, null=True)),
                ('vi_tri_13', models.IntegerField(blank=True, null=True)),
                ('vi_tri_14', models.IntegerField(blank=True, null=True)),
                ('vi_tri_15', models.IntegerField(blank=True, null=True)),
                ('vi_tri_16', models.IntegerField(blank=True, null=True)),
                ('DienAp_1', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_2', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_3', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_4', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_5', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_6', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_7', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_8', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_9', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_10', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_11', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_12', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_13', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_14', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_15', models.CharField(blank=True, max_length=20, null=True)),
                ('DienAp_16', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_1', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_2', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_3', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_4', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_5', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_6', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_7', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_8', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_9', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_10', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_11', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_12', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_13', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_14', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_15', models.CharField(blank=True, max_length=20, null=True)),
                ('CongSuat_16', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_1', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_2', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_3', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_4', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_5', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_6', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_7', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_8', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_9', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_10', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_11', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_12', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_13', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_14', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_15', models.CharField(blank=True, max_length=20, null=True)),
                ('DongDien_16', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_1', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_2', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_3', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_4', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_5', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_6', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_7', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_8', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_9', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_10', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_11', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_12', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_13', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_14', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_15', models.CharField(blank=True, max_length=20, null=True)),
                ('HieuSuat_16', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_API_read_write',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chuyen_Mach_Bang_Tay', models.BooleanField(default=False)),
                ('Thoi_Gian_Chay_Chuyen_Mach', models.TimeField(auto_now=True)),
                ('Thoi_Gian_Tat_Chuyen_Mach', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Data_API',
        ),
    ]
