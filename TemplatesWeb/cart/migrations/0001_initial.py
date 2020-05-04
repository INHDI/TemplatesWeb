# Generated by Django 2.2.12 on 2020-05-04 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ho_ten', models.CharField(blank=True, max_length=50, verbose_name='Họ Và Tên')),
                ('SDT', models.CharField(blank=True, max_length=50, verbose_name='Số Điện thoại')),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Dia_chi', models.TextField(blank=True)),
                ('Ghi_chu', models.TextField()),
                ('So_luong', models.PositiveSmallIntegerField(blank=True, default=1, max_length=5, verbose_name='Số lượng')),
                ('San_Pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.SPBanModel')),
            ],
        ),
    ]
