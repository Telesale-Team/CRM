# Generated by Django 3.2.3 on 2023-06-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0059_auto_20230619_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='ชื่อจริง'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='นามสกุล'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='password',
            field=models.CharField(blank=True, max_length=100, verbose_name='พาสเวิร์ด'),
        ),
    ]
